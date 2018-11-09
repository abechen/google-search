# encoding=utf-8
import pytest

import google_search

def test_get():
    result = google_search.get("Taiwan", page=1)

    assert len(result) == 10