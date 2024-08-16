#!/usr/bin/env python3
"""a module
"""
import csv
import math
from typing import List, Tuple


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
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        self.dataset()
        t = index_range(page, page_size)
        if t[0] > len(self.__dataset):
            return []
        return self.__dataset[t[0]:t[1]]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index range
    """
    if page == 1:
        return (0, page_size)
    return ((page * page_size) - page_size, page * page_size)


child = Server()
child.dataset()
child.get_page(1, 2)
