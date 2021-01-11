#!/usr/bin/python3
"""
x-request-id module
"""
if __name__ == "__main__":
    import urllib.request
    from sys import argv
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
