"""
google_search.structures
~~~~~~~~~~~~

This module .

:copyright: (c) 2018 by Abe Chen.
"""
class Result(dict):

    def __init__(self, title=None, url=None, desc=None):
        self.title = title
        self.url = url
        self.desc = desc

    def __str__(self):
        return """
            title: {}\n
            url: {}\n
            desc: {}
        """.format(self.title, self.url, self.desc)

    def get(self, key, default=""):
        return self.__dict__.get(key, default)

    def to_json(self):
        return {
            'title': "".join(self.title) if self.title else "",
            'url': self.url,
            'desc': "".join(self.desc) if self.desc else ""
        }