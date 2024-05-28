import requests


def get_rss_feed(url: str) -> str:
    resp = requests.get(url)
    if resp.status_code != 200:
        raise Exception("rss feed returns status: ", resp.status_code)

    body = resp.text
    return body
