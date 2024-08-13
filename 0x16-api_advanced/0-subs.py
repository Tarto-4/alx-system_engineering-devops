#!/usr/bin/python3
"""
0-subs.py
Queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers (total subscribers) for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyRedditClient/0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Return 0 if the status code is not 200
    if response.status_code != 200:
        return 0

    try:
        # Extract the number of subscribers from the response
        return response.json().get('data', {}).get('subscribers', 0)
    except (ValueError, KeyError):
        # Return 0 if there's an issue with the response content
        return 0
