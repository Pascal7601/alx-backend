#!/usr/bin/env python3
"""
implements FIFO cache replacement policy
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache implements a caching system using the LIFO algorithm """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.last_key = None  # To keep track of the last inserted key

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.last_key = key  # Update the last inserted key

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # LIFO: Remove the last inserted item
                del self.cache_data[self.last_key]
                print(f"DISCARD: {self.last_key}")
                # Update last_key to the new last item in the cache
                self.last_key = list(self.cache_data.keys())[-1]

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
