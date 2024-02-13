#!/usr/bin/python3
"""queries the Reddit API and returns a list containing the titles of all
hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) Apple' +
        'WebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    r = requests.get('https://www.reddit.com/r/{:}/hot.json?after={:}'.format(
        subreddit, after), headers=headers, allow_redirects=False)
    if r.status_code == 200:
        json = r.json()
        data_dict = json.get('data')
        post_list = data_dict.get('children')
        for post in post_list:
            post_data_dict = post.get('data')
            hot_list.append(post_data_dict.get('title'))
        after = data_dict.get('after')
        if data_dict.get('after') is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None