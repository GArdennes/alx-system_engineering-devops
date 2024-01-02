#!/usr/bin/python3
"""Script that uses a REST API and returns information about an employee"""
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

    if todo_progress:
        employee_name = todo_progress['name']
        user_data = todo_progress['user']
        task_list = todo_progress['todos']
        total_tasks = len(task_list)
        done_tasks = [task for task in task_list if task.get('completed')]
        print(
                "Employee {} is done with tasks ({}/{}):".format(
                    employee_name, len(done_tasks), total_tasks))
        for task in done_tasks:
            print("\t {}".format(task['title']))
    else:
        print("Failed to retrieve TODO progress.")
