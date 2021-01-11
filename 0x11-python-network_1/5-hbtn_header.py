#!/usr/bin/python3
"""
retrieve x-requets-id with requests module
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))
