import xml.etree.ElementTree as ET
from datetime import datetime


def parse_rss_feed(xml: str) -> dict:
    root = ET.fromstring(xml)

    include = ["title", "link", "description", "pubDate"]
    rss_info = {}
    articles = []

    for channel in root.findall("channel"):
        title = channel.find("title")
        if title is not None:
            rss_info["publisher"] = title.text

        for item in channel.findall("item"):
            article = {}
            for each in item.findall("./*"):
                if each.tag in include:
                    value = each.text
                    if each.tag == "pubDate" and value is not None:
                        formatted_date = datetime.strptime(
                            value, "%a, %d %b %Y %I:%M:%S %Z"
                        ).strftime("%Y-%m-%d")
                        value = formatted_date
                    article[each.tag] = value
            articles.append(article)

    rss_info["articles"] = articles
    return rss_info
