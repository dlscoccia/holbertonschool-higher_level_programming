#!/usr/bin/python3
"""
fetcher module with requests
"""
if __name__ == "__main__":
    import requests
    r = requests.get('https://intranet.hbtn.io/status').text
    print('Body response:')
    print("\t- type: {}".format(type(r)))
    print("\t- content: {}".format(r))
