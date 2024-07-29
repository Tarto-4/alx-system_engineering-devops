#!/usr/bin/python3
import json
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
    username = user_data.get('username')

    # Fetch todos
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Prepare data for JSON
    tasks = []
    for task in todos_data:
        task_dict = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        }
        tasks.append(task_dict)
    json_data = {str(employee_id): tasks}

    # Write to JSON file
    with open(f"{employee_id}.json", 'w') as file:
        json.dump(json_data, file)
