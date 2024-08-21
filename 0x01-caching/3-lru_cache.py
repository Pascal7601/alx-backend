#!/usr/bin/env python3
"""
file to emulate Least
Recently used algorithm for
cAche replacemtn
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache implements a caching system using the LRU algorithm """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []  # To keep track of the usage order of keys

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update the key's position in the order list
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # LRU: Remove the least recently used item
                lru_key = self.order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            # Add the item to the cache and update the order list
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Update the key's position in the order list (move to the end)
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data.get(key)
