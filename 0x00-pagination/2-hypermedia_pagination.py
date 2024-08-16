#!/usr/bin/env python3
"""a module
"""
import csv
import math
from typing import List, Tuple, Dict


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
        if t[0] * t[1] > len(self.__dataset):
            return self.__dataset[t[0]:]
        return self.__dataset[t[0]:t[1]]
        # assert type(page) == int and type(page_size) == int
        # assert page > 0 and page_size > 0
        # start, end = index_range(page, page_size)
        # data = self.dataset()
        # if start > len(data):
        #     return []
        # return data[start:end]
        # assert type(page) is int and page > 0
        # assert type(page_size) is int and page_size > 0

        # indexes = index_range(page, page_size)
        # try:
        #     data = self.dataset()
        #     return data[indexes[0]: indexes[1]]
        # except IndexError:
        #     return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        myDict = {}
        listy = self.get_page(page, page_size)
        myDict["page_size"] = len(listy)
        myDict["page"] = page
        myDict["data"] = listy
        myDict["next_page"] = page + 1 if page * page_size < len(
            self.__dataset) else None
        myDict["prev_page"] = page - 1 if not page == 1 else None
        myDict["total_pages"] = int(
            len(self.__dataset) / page_size) + 1 if not len(
                self.__dataset) % page_size == 0 else len(
                    self.__dataset) / page_size
        return myDict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index range
    """
    if page == 1:
        return (0, page_size)
    return ((page * page_size) - page_size, page * page_size)
    # index_tuple = page_size * (page - 1), page * page_size
    # return index_tuple
