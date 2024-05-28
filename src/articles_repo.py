import csv
import os


class InFileArticlesRepo:
    def __init__(self, path: str):
        dir, _ = os.path.split(path)
        if not os.path.exists(dir):
            os.makedirs(dir)

        self.__db = open(path, "a+")

    def save(self, articles: list[dict]) -> None:
        writer = csv.DictWriter(
            self.__db, fieldnames=["title", "link", "description", "pubDate"]
        )
        for article in articles:
            writer.writerow(article)
