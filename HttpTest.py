import os.path
import time
import datetime
import requests
import sys


def callAUrl(url):
	try:
		response = requests.get(url)
		print response
	except Exception as e:
		raise e

def __main__():
	callAUrl("http://google.co.in")

__main__()