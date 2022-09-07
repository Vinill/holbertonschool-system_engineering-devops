#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress"""

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    arg = argv[1]
    get__user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(arg))
    get__name = (get__user.json().get("username"))
    var = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                       .format(arg))

    get__val = var.json()
    list_user = []
    dict_user = {arg: list_user}

    for task in get__val:
        list_user.append({"task": task.get('title'),
                          "completed": task.get('completed'),
                          "username": get__name})

    with open(arg + '.json', 'w', encoding='utf-8') as f:
        json.dump(dict_user, f)
