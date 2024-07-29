# 0x15. Python - API Advanced

This repository contains tasks related to fetching and exporting data from a REST API. The tasks involve using Python scripts to gather information about an employee's TODO list from a provided API and exporting the data in various formats.

## Tasks

### Task 0: Gather data from an API

**Script:** `0-gather_data_from_an_API.py`

Fetches data from the API and displays the TODO list progress of an employee specified by their ID.

#### Usage
```bash
./0-gather_data_from_an_API.py <employee_id>

Output Format

Employee <employee_name> is done with tasks(<number_of_done_tasks>/<total_number_of_tasks>):
    <task_title>
    ...

Task 1: Export to CSV

Script: 1-export_to_CSV.py

Fetches the TODO list data for a given employee and exports it to a CSV file.
Usage

./1-export_to_CSV.py <employee_id>

Output File

The file <employee_id>.csv will contain:

"<employee_id>","<username>","<task_completed_status>","<task_title>"
...

Task 2: Export to JSON

Script: 2-export_to_JSON.py

Fetches the TODO list data for a given employee and exports it to a JSON file.
Usage

./2-export_to_JSON.py <employee_id>

Output File

The file <employee_id>.json will contain:

{
    "<employee_id>": [
        {
            "task": "<task_title>",
            "completed": <task_completed_status>,
            "username": "<username>"
        },
        ...
    ]
}

Task 3: Dictionary of List of Dictionaries

Script: 3-dictionary_of_list_of_dictionaries.py

Fetches the TODO list data for all employees and exports it to a JSON file.
Usage

./3-dictionary_of_list_of_dictionaries.py

Output File

The file todo_all_employees.json will contain:

{
    "<employee_id>": [
        {
            "username": "<username>",
            "task": "<task_title>",
            "completed": <task_completed_status>
        },
        ...
    ],
    ...
}

API Used

The scripts interact with a mock API provided by JSONPlaceholder. The base URL is https://jsonplaceholder.typicode.com/.
Requirements

    Python 3.4+
    requests library

Installation

To install the requests library, run:

pip install requests

ontributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.
License

This project is licensed under the MIT License.