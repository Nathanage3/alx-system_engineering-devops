'''#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) Apple' +
        'WebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code >= 300:
        return 0   
    json_data = r.json()
    data_dict = json_data.get('data')
    return data_dict.get('subscribers')
    '''
#!/usr/bin/python3

import requests as r


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:73.0) \
        Gecko/20100101 Firefox/73.0"
    }
    response = r.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
