'''
Code specific to accessing the Common Crawl index
'''
import time
import gzip
import logging
import warnings

from .myrequests import myrequests_get
from .timestamp import time_to_timestamp, timestamp_to_time, pad_timestamp_up

LOGGER = logging.getLogger(__name__)


def get_cc_endpoints():
    # TODO: cache me
    r = myrequests_get('https://index.commoncrawl.org/collinfo.json')
    if r.status_code != 200:
        raise RuntimeError('error getting list of common crawl indices: '+str(r.status_code))  # pragma: no cover

    j = r.json()
    endpoints = [x['cdx-api'] for x in j]
    if len(endpoints) < 30:  # last seen to be 39
        raise ValueError('Surprisingly few endpoints for common crawl index')  # pragma: no cover

    # endpoints arrive sorted oldest to newest, but let's force that anyawy
    endpoints = sorted(endpoints)

    return endpoints


def apply_cc_defaults(params, now=None):
    three_months = 3 * 30 * 86400
    year = 365*86400
    if params.get('from_ts') is None:
        if params.get('closest') is not None:
            closest_t = timestamp_to_time(params['closest'])
            params['from_ts'] = time_to_timestamp(closest_t - three_months)
            LOGGER.info('no from but closest, setting from=%s', params['from_ts'])
            if params.get('to') is None:
                params['to'] = time_to_timestamp(closest_t + three_months)
                LOGGER.info('no to but closest, setting to=%s', params['to'])
        elif params.get('to') is not None:
            to = pad_timestamp_up(params['to'])
            params['from_ts'] = time_to_timestamp(timestamp_to_time(to) - year)
            LOGGER.info('no from but to, setting from=%s', params['from_ts'])
        else:
            if not now:
                now = time.time()
            params['from_ts'] = time_to_timestamp(now - year)
            LOGGER.info('no from, setting from=%s', params['from_ts'])
    if params.get('to') is None:
        if params.get('closest') is not None:
            closest_t = timestamp_to_time(params['closest'])
            # 3 months later
            params['to'] = time_to_timestamp(closest_t + three_months)
            LOGGER.info('no to but closest, setting from=%s', params['to'])
        else:
            # no to or closest; from was set above, we will not set to
            pass


def fetch_warc_content(capture):
    warnings.warn("this API is not finalized", DeprecationWarning)

    filename = capture['filename']
    offset = int(capture['offset'])
    length = int(capture['length'])

    cc_external_prefix = 'https://commoncrawl.s3.amazonaws.com'
    url = cc_external_prefix + '/' + filename
    headers = {'Range': 'bytes={}-{}'.format(offset, offset+length-1)}

    resp = myrequests_get(url, headers=headers)
    record_bytes = resp.content

    # WARC digests can be represented in multiple ways (rfc 3548)
    # I have code in a pullreq for warcio that does this comparison
    #if 'digest' in capture and capture['digest'] != hashlib.sha1(content_bytes).hexdigest():
    #    LOGGER.error('downloaded content failed digest check')

    if record_bytes[:2] == b'\x1f\x8b':
        # XXX We should respect Content-Encoding here, and not just blindly ungzip
        record_bytes = gzip.decompress(record_bytes)

    # hack the WARC response down to just the content_bytes
    try:
        warcheader, httpheader, content_bytes = record_bytes.strip().split(b'\r\n\r\n', 2)
    except ValueError:  # pragma: no cover
        # not enough values to unpack
        return b''

    # XXX help out with the page encoding? complicated issue.
    return content_bytes
