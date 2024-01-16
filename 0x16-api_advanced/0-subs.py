#!/usr/bin/python3
"""Script that queries a Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API
    Args:
    subreddit(str): name of the subreddit
    Returns:
    int: the number of subscribers, or 0 if subreddit is invalid
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        if response.status_code == 200:
            data = response.json()
            return data.get('data').get('subscribers')
        else:
            return 0
    except requests.exceptions.RequestException as error:
        return 0
