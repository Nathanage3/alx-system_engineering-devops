#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""

import requests
import sys

def top_ten(subreddit):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) Apple' +
        'WebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception if status code >= 400
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        
        for post in posts:
            title = post.get('data', {}).get('title', '')
            print(title)
            if not posts:
                print("None")
    except requests.RequestException as e:
        print(f"Error: {e}")
