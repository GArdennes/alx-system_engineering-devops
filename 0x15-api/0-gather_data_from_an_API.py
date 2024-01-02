#!/usr/bin/python3
"""Script that uses a REST API to print the employee ID"""
import requests
from sys import argv


def get_todo_progress():
    """
    Retrieves TODO list progress for the specified employee
    """
    employee_id = int(argv[1])
    url1 = 'https://jsonplaceholder.typicode.com/users/{}'.format(
            employee_id)
    url2 = '{}/todos'.format(url1)
    todo_list = requests.get(url2).json()
    user = requests.get(url1).json()
    done_tasks = [task for task in todo_list if task.get('completed')]
    print(
            "Employee {} is done with tasks({}/{}): ".format(
                user.get('name'),
                len(done_tasks),
                len(todo_list)))
    for todo in done_tasks:
        print("\t {}".format(todo.get('title')))


if __name__ == '__main__':
    todo_list = get_todo_progress()
