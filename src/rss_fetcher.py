import requests


def get_rss_feed(url: str) -> str:
    resp = requests.get(url)
    if resp.status_code != 200:
        raise Exception("rss feed returns status: ", resp.status_code)

    body = resp.text
    return body


def get_multi_rss_feeds(urls: list[str]) -> list[str]:
    raw_feeds = []
    for url in urls:
        raw_feed = get_rss_feed(url)
        raw_feeds.append(raw_feed)
    return raw_feeds
