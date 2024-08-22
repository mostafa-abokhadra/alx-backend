#!/usr/bin/env python3
"""least frequently used
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ the logic is as follow:
        - when we first put or add into cahce_data, we will put
        the same element key in the lfu_lru dictionary with the 
        value of 1 (indicating only one operation have been
        done on that key which is the addition operation till now)
        -whenever that key is used again either by
        put function(updating it's value) or by get function
        we will increment it's value by +1 and at the same time
        we will move it at the beginning of the dictionary indicating
        the most recently used
        - when we reach the limits, we will loop on the values of
        lfu_lru dictionary and find the minimum value which indicates
        the least frequently used, then we will count how many times this
        minumum number is repeated as another keys value, if it exists only
        once then we will just remove this item, if it is repeated
        more than one time as multiple keys value we will remove the item
        according to the recency by looping on the dictionary from the end
        and find the first occurance of the minimum value from the end which
        indicates the least recently used
        (lastkeys in the dictionary is the older keys)
        -Note that when we tried to find the minimum value of dict.values()
        we started from index 1, because index 0 is for the new item which 
        is just added right now so it's counter gonna be 1, so exclude that
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
