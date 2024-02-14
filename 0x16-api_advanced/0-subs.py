#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers (total subscribers) for the subreddit. Returns 0 if invalid subreddit.
    """
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) Apple' +
        'WebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }

    # Construct the API URL for the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        # Make the API request
        response = requests.get(url, headers=headers)
        data = response.json()

        # Check if the subreddit exists
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0  # Invalid subreddit
    except requests.RequestException:
        return 0  # Error occurred or invalid subreddit
