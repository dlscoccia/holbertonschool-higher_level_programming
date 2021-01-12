#!/usr/bin/python3
"""
script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth
    user_name = argv[1]
    passwd = argv[2]
    url = "https://api.github.com/users/" + user_name
    response = requests.get(url, auth=HTTPBasicAuth(user_name, passwd))
    try:
        print(response.json().get('id'))
    except KeyError:
        print("None")
