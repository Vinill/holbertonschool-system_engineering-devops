#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    get__user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(argv[1]))
    get__name = (get__user.json().get("name"))
    var = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                       .format(argv[1]))
    get__val = var.json()
    get__len__val = len(get__val)
    res = []
    count = 0
    for task in get__val:
        if task["completed"] is True:
            res.append(task.get("title"))
            count += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(get__name, count, get__len__val))

    for title in res:
        print("\t {}".format(title))
