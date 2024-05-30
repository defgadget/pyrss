from typing import List, Optional


class Item:
    title: Optional[str]
    link: Optional[str]
    description: Optional[str]
    pub_date: Optional[str]
    guid: Optional[str]

    def __init__(
        self,
        title: Optional[str],
        link: Optional[str],
        description: Optional[str],
        pub_date: Optional[str],
        guid: Optional[str],
    ) -> None:
        if description is None and title is None:
            raise ValueError(
                "valid rss/channel/item must contain one of either description or title"
            )
        self.title = title
        self.link = link
        self.description = description
        self.pub_date = pub_date
        self.guid = guid


class Channel:
    title: str
    link: str
    description: str
    language: Optional[str]
    pub_date: Optional[str]
    last_build_date: Optional[str]
    docs: Optional[str]
    generator: Optional[str]
    managing_editor: Optional[str]
    web_master: Optional[str]
    item: List[Item]

    def __init__(
        self,
        title: str,
        link: str,
        description: str,
        language: str,
        pub_date: str,
        last_build_date: str,
        docs: str,
        generator: str,
        managing_editor: str,
        web_master: str,
        item: List[Item],
    ) -> None:
        self.title = title
        self.link = link
        self.description = description
        self.language = language
        self.pub_date = pub_date
        self.last_build_date = last_build_date
        self.docs = docs
        self.generator = generator
        self.managing_editor = managing_editor
        self.web_master = web_master
        self.item = item


class RSS:
    channel: Channel
    version: str

    def __init__(self, channel: Channel, version: str) -> None:
        self.channel = channel
        self.version = version


class Welcome2:
    rss: RSS

    def __init__(self, rss: RSS) -> None:
        self.rss = rss
