#!/usr/bin/python3
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    users_url = f"{base_url}users"
    todos_url = f"{base_url}todos"

    # Fetch all users
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Fetch all todos
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Prepare data for JSON
    all_data = {}
    for user in users_data:
        user_id = user.get('id')
        username = user.get('username')
        tasks = []
        for task in todos_data:
            if task.get('userId') == user_id:
                task_dict = {
                    "username": username,
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                tasks.append(task_dict)
        all_data[str(user_id)] = tasks

    # Write to JSON file
    with open("todo_all_employees.json", 'w') as file:
        json.dump(all_data, file)
