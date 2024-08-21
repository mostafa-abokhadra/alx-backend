#!/usr/bin/env python3
""" fifo caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """FiFO cache class
    """
    last_modified = ''

    def __init__(self):
        """class constructor
        """
        super().__init__()

    def put(self, key, item):
        """ adding to the cache system
        """
        last_modified = ''
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) == super().MAX_ITEMS:
            LIFOCache.last_modified = key

        if len(self.cache_data) > super().MAX_ITEMS:
            # deleted = list(self.cache_data.keys())[-2]
            del self.cache_data[LIFOCache.last_modified]
            print(f"DISCARD: {LIFOCache.last_modified}")
            LIFOCache.last_modified = key

    def get(self, key):
        """getting an item from the cached system
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]
