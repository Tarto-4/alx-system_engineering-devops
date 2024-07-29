#!/usr/bin/python3
"""
This module fetches TODO list data for all employees from the JSONPlaceholder API
and exports the data to a JSON file.

Usage:
    ./3-dictionary_of_list_of_dictionaries.py
"""

import json
import requests

def main():
    """
    Main function that retrieves employee and TODO data for all employees from the API,
    and writes the information to a JSON file.

    Args:
        None
    """
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    if users_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Could not retrieve data.")
        return

    users_data = users_response.json()
    todos_data = todos_response.json()

    all_data = {}

    for user in users_data:
        employee_id = user.get('id')
        employee_name = user.get('username')
        all_data[employee_id] = [{"task": task.get('title'), "completed": task.get('completed'), "username": employee_name} for task in todos_data if task.get('userId') == employee_id]

    json_filename = "todo_all_employees.json"

    with open(json_filename, 'w') as jsonfile:
        json.dump(all_data, jsonfile)

if __name__ == "__main__":
    main()
