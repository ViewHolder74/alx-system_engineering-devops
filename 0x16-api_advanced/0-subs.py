#!/usr/bin/python3
"""
0-subs.py
"""
import requests

def number_of_subscribers(subreddit):
	"""
	The function querries the Reddit API and
	return the number of subscribers(mot active users, total subscribers)
	dor a give subreddit.
	"""
	url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
	headers = {"User-Agent": "custom_user_agent"}

	response = requests.get(url, headers=headers)
	if (not response.ok):
		return 0
	sub_count = response.json().get('data').get('subscribers')
	return sub_count	
