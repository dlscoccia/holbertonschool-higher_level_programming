#!/usr/bin/python3
"""
Handling error codes
"""


if __name__ == "__main__":
    import urllib.request as request
    import urllib.error as error
    from sys import argv
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
