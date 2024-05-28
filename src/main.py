import rss_fetcher
from articles_repo import InFileArticlesRepo
from rss_parser import RSSParser


def main():
    xml = rss_fetcher.get_rss_feed(
        "https://cyber.harvard.edu/rss/examples/rss2sample.xml"
    )
    parser = RSSParser()
    rss = parser.parse_rss_feed(xml)
    print(rss["publisher"])
    print(rss["articles"])

    db = InFileArticlesRepo("./test/testdb.csv")
    db.save(rss["articles"])
    db.save(rss["articles"])


if __name__ == "__main__":
    main()
