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
    with open(arg + '.csv', 'w') as f:
        writer__file = csv.writer(f, quoting=csv.QUOTE_ALL)

        for task in get__val:
            writer__file.writerow([arg, get__name, task.get('completed'),
                                  task.get('title')])
