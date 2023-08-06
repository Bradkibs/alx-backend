#!/usr/bin/env python3

"""
fifo caching model
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ fifo caching algorithm"""

    def __init__(self):
        """ initializing the init method for fifocaching"""
        super().__init__()

    def put(self, key, item):
        """ creating a method to add items to the cache_data dict"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                first_element = next(iter(self.cache_data))
                self.cache_data.pop(first_element)
                print("DISCARD: {}".format(first_element))
        if key in self.cache_data:
            pass
        else:
            self.cache_data[key] = item
        return self.cache_data

    def get(self, key):
        """ getting key values from cached data"""
        if key is None or key not in self.cached_data:
            return None
        return self.cached_data.get(key)
