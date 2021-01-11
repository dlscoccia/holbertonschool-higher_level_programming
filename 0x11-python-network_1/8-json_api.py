#!/usr/bin/python3
'''
json with api post resquets
'''


if __name__ == "__main__":
    import requests
    from sys import argv
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    response = requests.post(url, data={'q': q})
    if response:
        json_response = response.json()
        id = json_response.get('id')
        name = json_response.get('name')
        if len(json_response) == 0 or not id or not name:
            print('No result')
        else:
            print('[{}] {}'.format(json_response.get('id'),
                                   json_response.get('name')))
    else:
        print('Not a valid JSON')
