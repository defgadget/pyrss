import unittest

import rss_parser


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
        parsed = rss_parser.parse_rss_feed(xml)
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
