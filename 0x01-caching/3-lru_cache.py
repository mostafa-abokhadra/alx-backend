#!/usr/bin/env python3
"""least recently used
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """lru class
    """
    lru = []

    def __init__(self):
        """initializer
        """
        super().__init__()

    def put(self, key, item):
        """adding to the cache
        """
        if key is None or item is None:
            return
        copy = self.cache_data.copy()
        self.cache_data[key] = item
        if len(copy) == len(self.cache_data):
            if not LRUCache.lru:
                LRUCache.lru.append(key)
            else:
                idx = LRUCache.lru.index(key)
                key = LRUCache.lru[idx]
                del LRUCache.lru[idx]
                LRUCache.lru.insert(0, key)
                # LRUCache.lru.insert(0, key)
                # del LRUCache.lru[0]
        else:
            LRUCache.lru.insert(0, key)

        if len(self.cache_data) > super().MAX_ITEMS:
            # print("got here")
            deleted = LRUCache.lru.pop()
            print(f"DISCARD: {deleted}")
            del self.cache_data[deleted]
            # print("put", LRUCache.lru)

    def get(self, key):
        """getting an item from cache
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        # print("bef", LRUCache.lru)
        idx = LRUCache.lru.index(key)
        key = LRUCache.lru[idx]
        del LRUCache.lru[idx]
        LRUCache.lru.insert(0, key)
        # print("aft", LRUCache.lru)
        return self.cache_data[key]
