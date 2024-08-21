#!/usr/bin/env python3
"""most recently used
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ the logic is as follow:
        literally the same as the least recently used
        but instead of poping out the last item from the
        lru list indicating the least recently used, we
        just poping out the first element of the list
        indicating most recently used, note that we don't
        pop list[0] but we pop out list[1] that is because we
        add the new item to the cache at the beginning of the
        self.cache_data before we actually empty the space
        so the item that need to be deleted moves from first
        postion to the second postion "list[1]"
    """
    mru = []

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
            if not MRUCache.mru:
                MRUCache.mru.append(key)
            else:
                idx = MRUCache.mru.index(key)
                key = MRUCache.mru[idx]
                del MRUCache.mru[idx]
                MRUCache.mru.insert(0, key)
                # MRUCache.mru.insert(0, key)
                # del MRUCache.mru[0]
        else:
            MRUCache.mru.insert(0, key)

        if len(self.cache_data) > super().MAX_ITEMS:
            # print("got here")
            # deleted = MRUCache.mru.pop()
            deleted = MRUCache.mru[1]
            print(f"DISCARD: {deleted}")
            del self.cache_data[deleted]
            del MRUCache.mru[1]
            # print("put", MRUCache.mru)

    def get(self, key):
        """getting an item from cache
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        # print("bef", MRUCache.mru)
        idx = MRUCache.mru.index(key)
        key = MRUCache.mru[idx]
        del MRUCache.mru[idx]
        MRUCache.mru.insert(0, key)
        # print("aft", MRUCache.mru)
        return self.cache_data[key]
