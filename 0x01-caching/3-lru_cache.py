#!/usr/bin/env python3
"""least recently used
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ the logic is as follow:
        - what ever operation (put, get, updata)
        happens on self.cache_data we will log
        these into the lru list
        - last item in lru will always be the
        least used so will be removed whenever
        cache reach it's maximum limits
        - if size of cache_data before and after
        put operation is the same this indicates
        an update operation not adding new value
        which has it's own logic
        - if size of cache_data after put operatoin
        is bigger than before this indicates
        adding new value which has it's own logic
        - whenever we "get", or "put" any item we
        will add this item to the front of the
        lru list meaning that this item is
        recently used so not to be considered when
        removal time comes, this will also make the last item
        of lru list always be the least recently used
        which we can pop from the list when time comes and
        from the cache_data
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
