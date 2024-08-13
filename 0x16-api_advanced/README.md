# 0x16. API Advanced

## Description

This repository contains solutions to tasks that involve querying the Reddit API using Python. The tasks are part of the ALX SE program and require implementing various functions to interact with the Reddit API, such as fetching subscriber counts, retrieving hot posts, and recursively getting all hot post titles for a subreddit.

## Project Structure

- **0-subs.py**: Contains the function `number_of_subscribers(subreddit)` that queries the Reddit API and returns the total number of subscribers for a given subreddit.
- **1-top_ten.py**: Contains the function `top_ten(subreddit)` that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
- **2-recurse.py**: Contains the recursive function `recurse(subreddit, hot_list=[])` that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.

## Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3.
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/python3`.
- Libraries imported in Python files must be organized in alphabetical order.
- The `README.md` file is mandatory at the root of the project folder.
- Code follows the PEP 8 style.
- All files are executable.
- The length of the files will be tested using `wc`.
- All modules include documentation.
- The `requests` module is used for sending HTTP requests to the Reddit API.

## Usage

To use the functions in this repository, you can import them into your Python script or run them directly from the command line using the provided test files:

```bash
# Example usage
$ python3 0-main.py programming
$ python3 1-main.py programming
$ python3 2-main.py programming

Files

    0-main.py: Test file for 0-subs.py.
    1-main.py: Test file for 1-top_ten.py.
    2-main.py: Test file for 2-recurse.py.

Author

Thato Mongwe - GitHub Profile
License

This project is licensed under the MIT License - see the LICENSE file for details.

less

`"https://github.com/tarto-4"`
