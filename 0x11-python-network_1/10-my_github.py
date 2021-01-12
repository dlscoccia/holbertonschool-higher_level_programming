#!/usr/bin/python3
'''
github api resquest id from user
'''


if __name__ == "__main__":
    import requests
    from sys import argv
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    r = r.json()
    try:
        print(r['id'])
    except KeyError:
        print("None")
