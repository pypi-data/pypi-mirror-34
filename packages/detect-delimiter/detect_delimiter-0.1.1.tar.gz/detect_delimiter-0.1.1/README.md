
# detect_delimiter

## About

Detects the delimiter used in CSV, TSV and other ad hoc file formats.

## Installation

Use `pip install detect_delimiter`

## Usage

`detect_delimiter` exposes the `detect()` functinon, which takes a `str`
as input and returns a delimiter.

    >>> from detect_delimiter import detect
    >>> detect("looks|like|the vertical bar\n is|the|delimiter\n")
    '|'

When `detect()` doesn't know, it returns `None`:

    >>> text = "not really any delimiters in here.\nthis is just text.\n"
    >>> detect()

It's possible to provide a default, which will be used in that case:

    >>> detect(text, default=',')
    ','


By default, `detect()` will prevent avoid checking alpha-numeric characters
and the period/full stop character ("."). This can be adjusted via 
the `blacklist` parameter.

If you believe that you know the delimiter, it's possible to provide
a list of possible delimiters to check for via the `whitelist` parameter.
If you don't provide a value, `[',', ';', ':', '|', '\t']` will be checked.

## Testing

You can either use `pytest` or `tox` directly from the project's root directory.