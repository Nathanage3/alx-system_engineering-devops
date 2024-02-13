#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    headers = {
        'User-Agent': 'Custom User Agent'
    }
    url = 'https://www.reddit.com/r/{:}/about.json'.format(
        subreddit)
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code >= 300:
        return 0
    json = r.json()
    data_dict = json.get('data')
    return(data_dict.get('subscribers'))