import datetime
import sys

try:
    from urllib.parse import urlparse
except ImportError:
    # python 2
    from urlparse import urlparse

PY2 = (sys.version_info.major == 2)


def parse_time(timestr):
    if not timestr:
        return datetime.datetime.utcnow()
    try:
        timestr = timestr.replace(' ', 'T')
        return datetime.datetime.strptime(timestr, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        return datetime.datetime.strptime(timestr, "%Y-%m-%dT%H:%M:%S")


def datestr(then, now=None):
    """Converts time to a human readable string.

    Wrapper over web.datestr.

        >>> from datetime import datetime
        >>> datestr(datetime(2010, 1, 2), datetime(2010, 1, 1))
        '1 day ago'
    """
    s = _web_datestr(then, now)
    if 'milliseconds' in s or 'microseconds' in s:
        s = 'Just now'
    return s


def _web_datestr(then, now=None):
    """
    datestr utility from web.py (public domain).

    source: https://github.com/webpy/webpy

    Converts a (UTC) datetime object to a nice string representation.

        >>> from datetime import datetime, timedelta
        >>> d = datetime(1970, 5, 1)
        >>> datestr(d, now=d)
        '0 microseconds ago'
        >>> for t, v in iteritems({
        ...   timedelta(microseconds=1): '1 microsecond ago',
        ...   timedelta(microseconds=2): '2 microseconds ago',
        ...   -timedelta(microseconds=1): '1 microsecond from now',
        ...   -timedelta(microseconds=2): '2 microseconds from now',
        ...   timedelta(microseconds=2000): '2 milliseconds ago',
        ...   timedelta(seconds=2): '2 seconds ago',
        ...   timedelta(seconds=2*60): '2 minutes ago',
        ...   timedelta(seconds=2*60*60): '2 hours ago',
        ...   timedelta(days=2): '2 days ago',
        ... }):
        ...     assert datestr(d, now=d+t) == v
        >>> datestr(datetime(1970, 1, 1), now=d)
        'January  1'
        >>> datestr(datetime(1969, 1, 1), now=d)
        'January  1, 1969'
        >>> datestr(datetime(1970, 6, 1), now=d)
        'June  1, 1970'
        >>> datestr(None)
        ''
    """
    def agohence(n, what, divisor=None):
        if divisor: n = n // divisor

        out = str(abs(n)) + ' ' + what       # '2 day'
        if abs(n) != 1: out += 's'           # '2 days'
        out += ' '                           # '2 days '
        if n < 0:
            out += 'from now'
        else:
            out += 'ago'
        return out                           # '2 days ago'

    oneday = 24 * 60 * 60

    if not then: return ""
    if not now: now = datetime.datetime.utcnow()
    if type(now).__name__ == "DateTime":
        now = datetime.datetime.fromtimestamp(now)
    if type(then).__name__ == "DateTime":
        then = datetime.datetime.fromtimestamp(then)
    elif type(then).__name__ == "date":
        then = datetime.datetime(then.year, then.month, then.day)

    delta = now - then
    deltaseconds = int(delta.days * oneday + delta.seconds + delta.microseconds * 1e-06)
    deltadays = abs(deltaseconds) // oneday
    if deltaseconds < 0: deltadays *= -1 # fix for oddity of floor

    if deltadays:
        if abs(deltadays) < 4:
            return agohence(deltadays, 'day')

        # Trick to display 'June 3' instead of 'June 03'
        # Even though the %e format in strftime does that, it doesn't work on Windows.
        out = then.strftime('%B %d').replace(" 0", "  ")

        if then.year != now.year or deltadays < 0:
            out += ', %s' % then.year
        return out

    if int(deltaseconds):
        if abs(deltaseconds) > (60 * 60):
            return agohence(deltaseconds, 'hour', 60 * 60)
        elif abs(deltaseconds) > 60:
            return agohence(deltaseconds, 'minute', 60)
        else:
            return agohence(deltaseconds, 'second')

    deltamicroseconds = delta.microseconds
    if delta.days: deltamicroseconds = int(delta.microseconds - 1e6) # datetime oddity
    if abs(deltamicroseconds) > 1000:
        return agohence(deltamicroseconds, 'millisecond', 1000)

    return agohence(deltamicroseconds, 'microsecond')


def truncate(text, width):
    if len(text) > width:
        text = text[:width-3] + "..."
    return text

def get_host_name(url):
    host = urlparse(url).netloc
    host_name = host.split(':')[0]
    return host_name
