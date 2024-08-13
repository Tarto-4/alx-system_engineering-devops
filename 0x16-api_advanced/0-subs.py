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
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        return 0
    
    data = response.json().get('data', {})
    return data.get('subscribers', 0)
