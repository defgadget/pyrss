import unittest

from rss_parser import RSSParser


class TestRSSParser(unittest.TestCase):
    def test_parse_rss_feed(self):
        xml = """<?xml version="1.0"?>
<rss version="2.0">
    <channel>
        <title>Test Title</title>
        <link>https://test.com</link>
        <item>
            <title>Test Article</title>
            <link>https://test.com/test</link>
            <description>This is a test description</description>
            <pubDate>Tue, 01 Jan 2024 11:06:42 GMT</pubDate>
        </item>
    </channel>
</rss>
"""
        parser = RSSParser()
        parsed = parser.parse_rss_feed(xml)
        expect = {
            "publisher": "Test Title",
            "articles": [
                {
                    "title": "Test Article",
                    "link": "https://test.com/test",
                    "description": "This is a test description",
                    "pubDate": "2024-01-01",
                }
            ],
        }
        self.assertDictEqual(parsed, expect)

    def test_parse_multi_rss_feeds(self):
        xml = """<?xml version="1.0"?>
<rss version="2.0">
    <channel>
        <title>Test Title</title>
        <link>https://test.com</link>
        <item>
            <title>Test Article</title>
            <link>https://test.com/test</link>
            <description>This is a test description</description>
            <pubDate>Tue, 01 Jan 2024 11:06:42 GMT</pubDate>
        </item>
    </channel>
</rss>
"""
        xml2 = """<?xml version="1.0"?>
<rss version="2.0">
    <channel>
        <title>Another Test Title</title>
        <link>https://anothertest.com</link>
        <item>
            <title>Another Test Article</title>
            <link>https://anothertest.com/test</link>
            <description>This is a test description</description>
            <pubDate>Tue, 01 Jun 2024 11:06:42 GMT</pubDate>
        </item>
    </channel>
</rss>
"""
        parser = RSSParser()
        parsed = parser.parse_multi_rss_feeds([xml, xml2])
        expect = [
            {
                "publisher": "Test Title",
                "articles": [
                    {
                        "title": "Test Article",
                        "link": "https://test.com/test",
                        "description": "This is a test description",
                        "pubDate": "2024-01-01",
                    }
                ],
            },
            {
                "publisher": "Another Test Title",
                "articles": [
                    {
                        "title": "Another Test Article",
                        "link": "https://anothertest.com/test",
                        "description": "This is a test description",
                        "pubDate": "2024-06-01",
                    }
                ],
            },
        ]
        self.assertListEqual(parsed, expect)

    def test_parse_rss_feed_with_custom_includes(self):
        xml = """<?xml version="1.0"?>
<rss version="2.0">
    <channel>
        <title>Test Title</title>
        <link>https://test.com</link>
        <item>
            <title>Test Article</title>
            <link>https://test.com/test</link>
            <description>This is a test description</description>
            <pubDate>Tue, 01 Jan 2024 11:06:42 GMT</pubDate>
        </item>
    </channel>
</rss>
"""
        parser = RSSParser(includes=["title", "link"])
        parsed = parser.parse_rss_feed(xml)
        expect = {
            "publisher": "Test Title",
            "articles": [
                {
                    "title": "Test Article",
                    "link": "https://test.com/test",
                }
            ],
        }
        self.assertDictEqual(parsed, expect)
