import csv
import os
import requests 
import xml.etree.ElementTree as ET

def save_to_csv(filename, data):
    exists = os.path.isfile(filename)
    with open(filename, "a", newline="") as csvfile:
        w = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        if not exists:
            header = ["Name", "URL"]
            w.writerow(header)
        w.writerow(data)

def read_from_csv(filename) -> list[str]:
    feed_list = []
    with open(filename, newline="") as csvfile:
        r = csv.reader(csvfile)
        r.__next__()
        for feeds in r:
            for feed in feeds:
                feed_list.append(feed)
    return feed_list
            
def fetch_rss_feed(url: str) -> str:
    if url == "":
        return ""
    r = requests.get(url)
    if r.status_code == 200:
        print("Success")
        return r.text
    else:
        print("Failed")
        return ""

def rss_xml_to_dict(content: str, newsfeeds:dict={}) -> dict:
    root = ET.fromstring(content)
    title = root.findtext("./channel/title")
    newsfeeds[title] = []
    for item in root.findall("./channel/item"):
        newsfeed = {}
        for child in item:
            newsfeed[child.tag] = child.text
        newsfeeds[title].append(newsfeed)
    return newsfeeds

def load_rss_feeds_list(csvfile: str) -> list:
    feed_list = read_from_csv(csvfile)
    print(feed_list)
    return feed_list

def download_rss_feeds(rss_urls: list) -> list[str]:
    rss_xml = []
    for url in rss_urls:
        rss_xml.append(fetch_rss_feed(url))
    return rss_xml

def main():
    feeds_database = "./rssfeeds.csv"
    rss_feeds = load_rss_feeds_list(feeds_database)
    rss_xml = download_rss_feeds(rss_feeds)
    newsfeeds = {}
    for xml in rss_xml:
        rss_xml_to_dict(xml, newsfeeds)
        
    for newsfeed in newsfeeds:
        print(newsfeed)


if __name__ == "__main__":
    main()

