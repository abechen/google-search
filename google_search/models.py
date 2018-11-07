"""
google_search.models
~~~~~~~~~~~~

This module .

:copyright: (c) 2018 by Abe Chen.
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from urllib import urlencode, unquote

from bs4 import BeautifulSoup

from .utils import default_headers, get_page, pause
from .structures import Result


class PreparedParser(object):

    def __init__(self):
        self.soup = None

    def prepare(self, html):

        self.prepare_soup(html)
    
    def prepare_soup(self, html):
        self.soup = BeautifulSoup(html, "html.parser")


class Parser(PreparedParser):

    def __init__(self):
        self.results = []
    
    def parse_results(self, html):
        self.prepare(
            html=html
        )

        for row in self.soup.select("div.g"):
            self.results.append(
                Result(
                    title=Parser.__get_title(row),
                    url=Parser.__get_url(row),
                    desc=Parser.__get_desc(row)
                )
            )

    @staticmethod
    def __get_title(row):
        tag = row.find("a")
        if tag:
            return tag.text.strip()

        return None

    @staticmethod
    def __get_url(row):
        def clean(url):
            clean_url = unquote(url)
            try:
                clean_url = clean_url.replace("/url?q=", "")
                clean_url = clean_url.split("&sa=")[0]
            finally:
                return clean_url

        tag = row.find("a")
        if tag:
            return clean(tag["href"])

        return None

    @staticmethod
    def __get_desc(row):
        tag_div = row.find("div", attrs={"class": "s"})
        if tag_div:
            tag_span = tag_div.find("span", attrs={"class": "st"})
            if tag_span is not None:
                return tag_span.text.strip()
        else:
            return None


class PreparedSearch(object):

    __SEARCH_URL = "https://www.google.com.tw/search?"

    def __init__(self):
        self.per_page = None
        self.start = None
        self.search_url = None

    def prepare(self,
            keyword=None,
            page=None,
            per_page=None):

        self.prepare_per_page(per_page)

        self.prepare_start(page, per_page)

        self.prepare_search_url(keyword)

    def prepare_per_page(self, per_page):
        self.per_page = per_page

    def prepare_start(self, page, per_page):
        self.start = page * per_page

    def prepare_search_url(self, keyword):
        params = {"q": keyword,
                  "num": self.per_page,
                  "lr": "lang_zh-TW",
                  "cr": "countryTW"}

        if self.start > 0: params["start"] = self.start

        self.search_url = "{}{}".format(PreparedSearch.__SEARCH_URL, urlencode(params))


class Search(PreparedSearch):

    def __init__(self):
        self.headers = default_headers()
        self.html = None

    def search(self, keyword, page, per_page=10, need_pause=True):
        self.prepare(
            keyword=keyword,
            page=page,
            per_page=per_page
        )

        self.html = get_page(self.search_url, self.headers)

        if need_pause:
            pause()

    @staticmethod
    def _get_result(html):
        parser = Parser()
        parser.parse_results(html)
        return parser.results
    
    def get(self, keyword, page, **kwargs):
        self.search(keyword, page, **kwargs)
        return Search._get_result(self.html)