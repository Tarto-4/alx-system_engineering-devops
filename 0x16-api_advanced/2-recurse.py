#!/usr/bin/python3
"""
2-recurse.py
Recursively queries the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit.
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively returns a list containing the titles of all hot articles
    for a given subreddit.
    If the subreddit is invalid, returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom-Agent'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return None
    
    data = response.json().get('data', {})
    children = data.get('children', [])
    
    for child in children:
        hot_list.append(child.get('data', {}).get('title', None))
    
    after = data.get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    
    return hot_list
