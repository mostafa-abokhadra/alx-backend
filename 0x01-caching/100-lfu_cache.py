#!/usr/bin/env python3
"""least frequently used
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ the logic is as follow:
    """
    lfu_lru = {}

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
            LFUCache.lfu_lru[key] = LFUCache.lfu_lru[key] + 1
            new_dict = dict({key: LFUCache.lfu_lru[key]})
            del LFUCache.lfu_lru[key]
            LFUCache.lfu_lru = {**new_dict, **LFUCache.lfu_lru}
        else:
            LFUCache.lfu_lru = {**{key: 1}, **LFUCache.lfu_lru}
            # print(LFUCache.lfu_lru)

        if len(self.cache_data) > super().MAX_ITEMS:
            deleted = ""
            leastFrequent = min(list(LFUCache.lfu_lru.values())[1:])
            # print(f"least is {leastFrequent}")
            checkSimilarFrequencey = list(
                LFUCache.lfu_lru.values()).count(leastFrequent)
            # print(f"similar is {checkSimilarFrequencey}")
            if checkSimilarFrequencey == 1:
                for key in LFUCache.lfu_lru.keys():
                    if LFUCache.lfu_lru[key] == leastFrequent:
                        deleted = key
                        del LFUCache.lfu_lru[key]
                        del self.cache_data[key]
                        break
            else:
                # print(f"reversed")
                # for key, value in reversed(LFUCache.lfu_lru.items()):
                #     print(key, "->", value)
                for k, v in reversed(LFUCache.lfu_lru.items()):
                    if v == leastFrequent:
                        deleted = k
                        del self.cache_data[k]
                        del LFUCache.lfu_lru[k]
                        break
            print(f"DISCARD: {deleted}")
            # print(LFUCache.lfu_lru)

    def get(self, key):
        """getting an item from cache
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        LFUCache.lfu_lru[key] += 1
        new_dict = dict({key: LFUCache.lfu_lru[key]})
        del LFUCache.lfu_lru[key]
        LFUCache.lfu_lru = {**new_dict, **LFUCache.lfu_lru}
        # print(LFUCache.lfu_lru)
        return self.cache_data[key]
