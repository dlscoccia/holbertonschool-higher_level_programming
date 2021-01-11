#!/usr/bin/python3
"""
POST module
"""


if __name__ == "__main__":
    import urllib.request as request
    import urllib.parse as parse
    from sys import argv
    url = argv[1]
    values = {'email': argv[2]}

    data = parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
