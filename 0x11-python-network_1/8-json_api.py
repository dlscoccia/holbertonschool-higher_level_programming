#!/usr/bin/python3
'''
json with api post resquets
'''


if __name__ == '__main__':
    import requests
    from sys import argv
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        req_json = req.json()
        id = req_json.get('id')
        name = req_json.get('name')
        if len(req_json) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(req_json.get('id'), req_json.get('name')))
    except:
        print("Not a valid JSON")
