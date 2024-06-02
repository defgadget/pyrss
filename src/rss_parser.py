import xml.etree.ElementTree as ET
from datetime import datetime


class RSSParser:
    def __init__(self, includes: list[str] = []):
        if len(includes) == 0 or includes is None:
            self.includes = ["title", "link", "description", "pubDate"]
        else:
            self.includes = includes

    def parse_rss_feed(self, xml: str) -> dict:
        xml = xml.strip()
        root = ET.fromstring(xml)

        rss_info = {}
        articles = []

        for channel in root.findall("channel"):
            title = channel.find("title")
            if title is not None:
                rss_info["publisher"] = title.text

            for item in channel.findall("item"):
                article = {}
                for each in item.findall("./*"):
                    if each.tag in self.includes:
                        value = ""
                        if each.text is not None:
                            value = each.text.strip()
                            if each.tag == "pubDate" and value is not None:
                                # formatted_date = datetime.strptime(
                                #     value, "%a, %d %b %Y %I:%M:%S %Z"
                                # ).strftime("%Y-%m-%d")
                                value = each.text.strip()
                        article[each.tag] = value
                articles.append(article)

        rss_info["articles"] = articles
        return rss_info

    def parse_multi_rss_feeds(self, xmls: list[str]) -> list[dict]:
        feeds = []
        for feed in xmls:
            parsed = self.parse_rss_feed(feed)
            feeds.append(parsed)
        return feeds
