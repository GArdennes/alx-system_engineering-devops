#!/usr/bin/python3
'''
Python script that uses a REST API, to get info for a given employee ID
'''
import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        user = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        req = requests.get("{}users/{}".format(url, user))
        j_son = req.json()
        name = j_son.get("username")
        if name is not None:
            jreq = requests.get(
                "{}todos?userId={}".format(
                    url, user)).json()
            completedtsk = []
            for t in jreq:
                tsk = {
                        'task': t.get('title'),
                        'completed': t.get('completed'),
                        'username': name
                        }
                completedtsk.append(tsk)
                d_task = {str(user): tsk}
                filename = '{}.json'.format(user)
                with open(filename, mode='w') as jsonfile:
                    json.dump(d_task, jsonfile)
