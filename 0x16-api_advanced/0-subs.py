#!/usr/bin/python3
"""
0-subs.py
Queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid or an error occurs, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyRedditClient/0.1'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise HTTPError for bad responses
        
        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    except (requests.RequestException, ValueError, KeyError) as e:
        # Log error if needed, e.g., print(e) for debugging
        return 0
