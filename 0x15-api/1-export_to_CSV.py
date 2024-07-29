#!/usr/bin/python3
"""
This module fetches TODO list data for a specified employee from the JSONPlaceholder API
and exports the data to a CSV file.

Usage:
    ./1-export_to_CSV.py <employee_id>
"""

import csv
import requests
import sys

def main():
    """
    Main function that retrieves employee and TODO data from the API,
    and writes the information to a CSV file.

    Args:
        None
    """
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
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

    employee_name = user_data.get('username')
    csv_filename = f"{employee_id}.csv"

    with open(csv_filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            csvwriter.writerow([employee_id, employee_name, task.get('completed'), task.get('title')])

if __name__ == "__main__":
    main()
