# 0-gather_data_from_an_API.py

#!/usr/bin/python3
"""
This module fetches data from the JSONPlaceholder API and prints
the progress of an employee's TODO list.

Usage:
    ./0-gather_data_from_an_API.py <employee_id>
"""

import requests
import sys


def main():
    """
    Main function that retrieves employee and TODO data from the API,
    calculates completed tasks, and prints the result.

    Args:
        None
    """
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        return

    employee_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Could not retrieve data.")
        return

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data.get('name')
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get('completed')]

    print(f"Employee {employee_name} is done with tasks "
          f"({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    main()

