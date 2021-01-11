#!/usr/bin/python3
"""
fetcher module decoded to str
"""
if __name__ == "__main__":
    import urllib.request as request
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read().decode('utf-8')
        print('Body response:')
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
