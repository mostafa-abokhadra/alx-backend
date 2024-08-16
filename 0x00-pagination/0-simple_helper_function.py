#!/usr/bin/env python3
"""a module
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index range
    """
    if page == 1:
        return (0, page_size)
    return ((page * page_size) - page_size, page * page_size)
