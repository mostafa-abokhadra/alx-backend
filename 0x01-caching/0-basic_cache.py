#!/usr/bin/env python3
""" a moudle
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic cache class
    """
    LIMITS: bool = False

    def __inti__(self):
        """constructor
        """
        super()

    def put(self, key, item):
        """ adding to the cache system
        """
        if key is None or item is None:
            self.cache_data[key] = item
            return

    def get(self, key):
        """
        """
        if key is None or self.cache_data.get(key) is None:
            return
        return self.cache_data.get(key)
