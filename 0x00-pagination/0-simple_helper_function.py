#!/usr/bin/env python3
"""
a python script that tries to emukate
pagiatation
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    function taht returns a start index and
    end index of a page
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
