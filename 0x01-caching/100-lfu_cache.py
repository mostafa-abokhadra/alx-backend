#!/usr/bin/env python3
"""least frequently used
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ the logic is as follow:
    """

    def __init__(self):
        """initializer
        """
        super().__init__()

    def put(self, key, item):
        """adding to the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > super().MAX_ITEMS:
            pass

    def get(self, key):
        """getting an item from cache
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]