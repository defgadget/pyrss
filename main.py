import csv
import os
import argparse
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

def read_from_csv(filename):
    with open(filename, newline="") as csvfile:
        r = csv.reader(csvfile)
        r.__next__()
        for row in r:
            print(", ".join(row))
            
def fetch_rss_feed(url: str) -> str:
    r = requests.get(url)
    if r.status_code == 200:
        print("Success")
        return r.text
    else:
        print("Failed")
        return ""

def parse_rss_xml(content: str) -> None:
    root = ET.fromstring(content)

    newsfeeds = {}
    title = root.findtext("./channel/title")
    newsfeeds[title] = []
    for item in root.findall("./channel/item"):
        newsfeed = {}
        for child in item:
            newsfeed[child.tag] = child.text
        newsfeeds[title].append(newsfeed)
    for nf in newsfeeds[title]:
        if "title" in nf:
            print(nf["title"])
        if "description" in nf:
            print(nf["description"])
        if "guid" in nf:
            print(nf["guid"])
        if "pubDate" in nf:
            print(nf["pubDate"])
        print()


def main():
    parser = argparse.ArgumentParser(description="PyRSS Manager")
    parser.add_argument("--file", nargs="?", default="database.csv")
    parser.add_argument("action", choices=["add", "delete", "list"])
    parser.add_argument
    args = parser.parse_args()
    db = args.file.lower()
    data = ["Sports Illustrated", "https://www.sportsillustrated.com"]

    if args.action.lower() == "add":
        save_to_csv(db, data)
    elif args.action.lower() == "list":
        read_from_csv(db)
    else:
        print("Unknow action")
        return


if __name__ == "__main__":
    content = fetch_rss_feed("https://www.rssboard.org/files/sample-rss-2.xml")
    parse_rss_xml(content)
