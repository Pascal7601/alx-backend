#!/usr/bin/env python3
"""
a python script that tries to emukate
pagiatation
"""
import csv
from typing import List, Tuple, Dict, Any
import math


def index_range(page: int, page_size: int) -> tuple:
    """
    function taht returns a start index and
    end index of a page
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset (i.e., the correct list of rows).

        Args:
        - page (int): The current page number.
        - page_size (int): The number of items per page.

        Returns:
        - List[List]: A list of lists representing sted page.
        """
        # Validate inputs
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        # Get the correct index range
        start_index, end_index = index_range(page, page_size)

        # Return the appropriate page of the dataset
        data = self.dataset()
        if start_index >= len(data):
            return []  # Return an empty list if start_index

        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Return a dictionary containing pagination information."""
        data_page = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": page_size,
            "page": page,
            "data": data_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
