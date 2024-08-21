#!/usr/bin/env python3
"""
implements FIFO cache replacement policy
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache inherits from BaseCaching and is a cachin
    system that uses FIFO algorithm.
    When the cache exceeds its maximum size, the first added item is discarded.
    """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []  # This will track the order of the keys

    def put(self, key, item):
        """
        Add an item to the cache.
        If the cache exceeds MAX_ITEMS, discard the first added item.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)

        self.cache_data[key] = item

        # Check if the cache exceeds the maximum number of items
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # FIFO: Remove the first item in the order list
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """
        Retrieve an item from the cache.
        Return None if key is None or doesn't exist.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
