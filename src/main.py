import rss_fetcher
from articles_repo import InFileArticlesRepo
from rss_feeds_repo import InFileRSSFeedsRepo
from rss_parser import RSSParser

__FEEDS_DB_PATH = "test/feeds.csv"
__ARTICLES_DB_PATH = "test/articles.csv"


def main():
    feeds_db = "test/feeds.csv"  # __FEEDS_DB_PATH
    feeds_repo = InFileRSSFeedsRepo(feeds_db)
    feeds_repo.add_feed("https://www.usda.gov/rss/latest-blogs.xml")
    feeds_repo.add_feed("https://www.usda.gov/rss/latest-releases.xml")

    articles_db = __ARTICLES_DB_PATH
    articles_repo = InFileArticlesRepo(articles_db)

    feeds = feeds_repo.get_feeds()
    feeds_xml = rss_fetcher.get_multi_rss_feeds(feeds)

    rss_parser = RSSParser()
    parsed_feeds = rss_parser.parse_multi_rss_feeds(feeds_xml)
    for feed in parsed_feeds:
        print(feed["publisher"])
    articles_repo.write(parsed_feeds)
    all_articles = articles_repo.get_all()
    for article in all_articles:
        print(article)


if __name__ == "__main__":
    main()
