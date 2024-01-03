#!/usr/bin/python3
"""Script that uses a REST API and returns information about an employee"""
import csv
import requests
from sys import argv


def get_todo_progress(employee_id):
    """
    Retrieves TODO list progress for the employee
    Args:
    employee_id: the ID of the employee
    Returns:
    dict: A dictionary containing the TODO list
    """
    url = "https://jsonplaceholder.typicode.com/"
    api_url = f"{url}users/{employee_id}"
    todo_url = f"{api_url}/todos"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        todo_data = response.json()
        name = todo_data.get('name')
        todo_list = requests.get(todo_url).json()
        if name is not None:
            return {'user': todo_data, 'name': name, 'todos': todo_list}
        else:
            print("Name is none")
    except requests.exceptions.RequestException as err:
        print("Error: Could not retrieve TODO data", err)
        return None


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        exit(1)
    employee_id = int(argv[1])
    todo_progress = get_todo_progress(employee_id)
    path = "{}.csv".format(employee_id)

    if todo_progress:
        user_data = todo_progress['user']
        todo_list = todo_progress['todos']
        with open(path, 'w', encoding='utf-8') as csvfile:
            writer = csv.writer(
                    csvfile,
                    delimiter=',',
                    quoting=csv.QUOTE_ALL)
            for todo in todo_list:
                writer.writerow([
                    employee_id,
                    user_data.get('username'),
                    todo.get('completed'),
                    todo.get('title')
                    ])
    else:
        print("Failed to retrieve TODO progress.")
