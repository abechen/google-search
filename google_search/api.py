"""
google_search.api
~~~~~~~~~~~~

This module implements the Google Search API.

:copyright: (c) 2018 by Abe Chen.
"""
from . import models

def get(keyword, page, **kwargs):
    r"""Get a google search one page result.
    :param keyword: the word that you would search from google.
    :param page: the page for the search result.
    :param per_page: (optional) per page count of search result.
    :param need_pause: (optional) default is True to avoid to be ban from google.
    :param \*\*kwargs: Optional arguments.
    :return: :class:`structures <Result>` object
    :rtype: dict(structures.Result)

    Usage::
      >>> import google_search
      >>> result = google_search.get(
                        keyword="google",
                        page=1
                    )
    """
    return models.Search().get(keyword, page, **kwargs)