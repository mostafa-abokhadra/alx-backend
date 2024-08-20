#!/usr/bin/env python3
""" a moudle
"""
BaseCaching = __import__('base_caching').BaseCaching


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
            return
        self.cache_data[key] = item

    def get(self, key):
        """ geting a cached data
        """
        if key is None or self.cache_data.get(key) is None:
            return
        return self.cache_data.get(key)
