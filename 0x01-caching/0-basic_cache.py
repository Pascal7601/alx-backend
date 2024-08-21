#!/usr/bin/env python3
"""
file that sets up the base for
caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    inherits from BaseCaching and implements
    the put and get method
    """
    def put(self, key, item):
        """
        adds data in the cahed_data dict
        """
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        returns the value of the key
        in the cached_data
        """
        if key is None:
            return None
        return self.cache_data.get(key)
