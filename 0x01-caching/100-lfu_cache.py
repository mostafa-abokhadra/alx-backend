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
            LFUCache.lfu_lru.updata(new_dict)
        else:
            LFUCache.lfu_lru.update({key: 1})

        if len(self.cache_data) > super().MAX_ITEMS:
            leastFrequent = min(list(LFUCache.lfu_lru.values()))
            checkSimilarFrequencey = (LFUCache.lfu_lru.values()).count(leastFrequent)
            if checkSimilarFrequencey == 1:
                for key in LFUCache.lfu_lru.keys():
                    if LFUCache.lfu_lru[key] == leastFrequent:
                        del LFUCache.lfu_lru[key]
                        del self.cache_data[key]
                        break
            else:
                for k in reversed(LFUCache.lfu_lru):
                    if k == key:
                        del self.cache_data[k]
                        del LFUCache.lfu_lru[k]
                        break

    def get(self, key):
        """getting an item from cache
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        LFUCache.lfu_lru[key] += 1
        new_dict = dict({key :LFUCache.lfu_lru[key]})
        del LFUCache.lfu_lru[key]
        LFUCache.lfu_lru.update(new_dict)
        return self.cache_data[key]