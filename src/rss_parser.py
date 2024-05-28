import xml.etree.ElementTree as ET


def parse_rss_feed(xml: str) -> dict:
    print("Parsing xml: ", f"{xml[:15]}...")
    root = ET.fromstring(xml)

    rss_info = {}
    articles = []
    for channel in root.findall("channel"):
        title = channel.find("title")
        if title is not None:
            rss_info["feed name"] = title.text
        for item in channel.findall("item"):
            article = {}
            for each in item.findall("./*"):
                match each.tag:
                    case "title":
                        article["title"] = each.text
                    case "link":
                        article["url"] = each.text
                    case "description":
                        article["summary"] = each.text
            articles.append(article)

    rss_info["articles"] = articles
    return rss_info
