import csv
import os


class InFileRSSFeedsRepo:
    def __init__(self, path: str):
        dir, _ = os.path.split(path)
        if not os.path.exists(dir):
            os.makedirs(dir)
        if not os.path.exists(path):
            f = open(path, "x")
            f.close()
        self.__db = path

    def add_feed(self, url: str, name: str = "") -> None:
        id_count = 1
        with open(self.__db, "r") as db:
            reader = csv.DictReader(db, fieldnames=["id", "name", "url"])
            for feed in reader:
                if feed["url"] == url:
                    print("feed already exists")
                    return
                id_count += 1
        feed = {
            "id": id_count,
            "name": name,
            "url": url,
        }
        with open(self.__db, "a") as db:
            writer = csv.DictWriter(db, fieldnames=["id", "name", "url"])
            writer.writerow(feed)

    def delete_feed(self, id: int) -> None:
        updated_feeds = []
        with open(self.__db, "r") as db:
            reader = csv.DictReader(db, fieldnames=["id", "name", "url"])
            for feed in reader:
                if feed["id"] == f"{id}":
                    continue
                updated_feeds.append(feed)
        with open(self.__db, "w") as db:
            writer = csv.DictWriter(db, fieldnames=["id", "name", "url"])
            writer.writerows(updated_feeds)

    def get_feeds(self) -> list[dict]:
        feeds = []
        with open(self.__db, "r") as db:
            reader = csv.DictReader(db, fieldnames=["id", "name", "url"])
            for feed in reader:
                feeds.append(feed)
        return feeds
