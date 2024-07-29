#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = f"{base_url}users/{employee_id}"
    todos_url = f"{base_url}todos?userId={employee_id}"

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch todos
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate task completion
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get('completed')]
    num_done_tasks = len(completed_tasks)

    # Print output
    print(f"Employee {employee_name} is done with tasks({num_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
