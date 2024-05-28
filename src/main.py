import rss_fetcher
import rss_parser


def main():
    xml = rss_fetcher.get_rss_feed(
        "https://cyber.harvard.edu/rss/examples/rss2sample.xml"
    )
    rss = rss_parser.parse_rss_feed(xml)
    print(rss["feed name"])
    print(rss["articles"])


if __name__ == "__main__":
    main()
