#!/usr/bin/python3
"""Script that queries a Reddit API"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API
    Args:
    subreddit (str): the name of the subreddit
    Return:
    str: prints the titles of the 10 hot posts else None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Google Chrome'}
    params = {'limit': 10}
    try:
        response = requests.get(
                url,
                headers=headers,
                allow_redirects=False,
                params=params
                )
        response.raise_for_status()
        if response.status_code == 200:
            results = response.json()
            my_data = results.get('data').get('children')
            for item in my_data:
                print(item.get('data').get('children'))
        else:
            print('None')
    except requests.exceptions.RequestException as error:
        print('None')
