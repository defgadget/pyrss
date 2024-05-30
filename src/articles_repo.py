import csv
import os
import time


class InFileArticlesRepo:
    fieldnames = [
        "id",
        "publisher",
        "title",
        "link",
        "description",
        "pubDate",
        "is_read",
    ]

    def __init__(self, path: str):
        dir, _ = os.path.split(path)
        if not os.path.exists(dir):
            os.makedirs(dir)
        if not os.path.exists(path):
            f = open(path, "x")
            f.close()

        self.__db = path

    def get_all(self) -> list[dict]:
        articles = []
        with open(self.__db, "r") as db:
            reader = csv.DictReader(db)
            for row in reader:
                articles.append(row)

        return articles

    def get_by_publisher(self, publisher: str) -> list[dict]:
        with open(self.__db, "r") as db:
            reader = csv.DictReader(db, fieldnames=self.fieldnames)
            articles = []
            for row in reader:
                if row["publisher"] == publisher:
                    articles.append(row)
            return articles

    def get_unread(self) -> list[dict]:
        with open(self.__db, "r") as db:
            reader = csv.DictReader(db, fieldnames=self.fieldnames)
            articles = []
            for row in reader:
                if row["is_read"] == "False":
                    articles.append(row)
            return articles

    def mark_read(self, rss: dict) -> None:
        articles = []
        with open(self.__db, "r") as db:
            reader = csv.DictReader(db, fieldnames=self.fieldnames)
            for row in reader:
                if row["id"] == rss["id"]:
                    row["is_read"] = True
                articles.append(row)
        with open(self.__db, "w") as db:
            writer = csv.DictWriter(db, fieldnames=self.fieldnames)
            writer.writerows(articles)

    def write(self, rss_list: list[dict]) -> None:
        id_count = 0
        with open(self.__db, "r") as db:
            reader = csv.DictReader(db)
            for _ in reader:
                id_count += 1

        with open(self.__db, "a+") as db:
            writer = csv.DictWriter(db, fieldnames=self.fieldnames)
            for rss in rss_list:
                publisher = rss["publisher"]
                for i, article in enumerate(rss["articles"], start=1):
                    article["id"] = i + id_count
                    article["publisher"] = publisher
                    article["is_read"] = False
                    writer.writerow(article)
