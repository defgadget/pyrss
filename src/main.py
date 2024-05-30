import rss_fetcher
from articles_repo import InFileArticlesRepo
from rss_parser import RSSParser


def main():
    xml = rss_fetcher.get_rss_feed(
        "https://cyber.harvard.edu/rss/examples/rss2sample.xml"
    )
    parser = RSSParser()
    rss = parser.parse_rss_feed(xml)

    db = InFileArticlesRepo("./test/testdb.csv")
    db.write([rss])
    article = {"id": "1"}
    db.mark_read(article)
    article2 = {"id": "2"}
    db.mark_read(article2)
    all_articles = db.get_all()
    unread_articles = db.get_unread()

    print(len(all_articles))
    print(len(unread_articles))


if __name__ == "__main__":
    main()
