import requests


def callAUrl(url):
    try:
        response = requests.get(url)
        print response.text
    except Exception as e:
        raise e



callAUrl("http://google.co.in")
