#!/usr/bin/python3
"""
1-top_ten.py
"""
import requests


def top_ten(subreddit):
	"""
	Queries the Reddit API and prints the titles of the first 10 hot posts
	listed for a given subreddit.
	"""
	url = 'https://www.reddit.com/r/{}/hot.json?show="all"&limit=10'.format(
        subreddit)
	headers = {'User-Agent': 'Custome-Agent'}
	response = requests.get(url, headers=headers)
	try:
		top_ten = response.json()['data']['children']
		for post in top_ten:
			print(post['data']['title'])
	except KeyError:
		print("None")
