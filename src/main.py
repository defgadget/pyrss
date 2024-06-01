import rss_fetcher
from articles_repo import InFileArticlesRepo
from rss_feeds_repo import InFileRSSFeedsRepo
from rss_parser import RSSParser


def main():
    feeds_db = "test/feeds.csv"
    feeds_repo = InFileRSSFeedsRepo(feeds_db)
    feeds_repo.add_feed("https://www.usda.gov/rss/latest-releases.xml", "USDA Latest")
    all_feeds = feeds_repo.get_feeds()
    print(all_feeds)
    feeds_repo.delete_feed(1)
    all_feeds = feeds_repo.get_feeds()
    print(all_feeds)


if __name__ == "__main__":
    main()
