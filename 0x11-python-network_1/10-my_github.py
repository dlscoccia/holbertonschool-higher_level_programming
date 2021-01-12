#!/usr/bin/python3
'''
github api resquest id from user
'''


if __name__ == "__main__":
    import requests
    from sys import argv
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(argv[1], argv[2]))
    req = req.json()
    try:
        print(req['id'])
    except KeyError:
        print("None")
