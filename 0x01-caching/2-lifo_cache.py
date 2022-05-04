#!/usr/bin/env python3
"""
    This module defines a class that is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Implements LIFO caching system that inherits from base_caching"""

    def __init__(self):
        """Initializes the class"""
        BaseCaching.__init__(self)
        self.last = ""

    def put(self, key, item):
        """Inserts items to cache and removes last inserted element
        if number of elements exceeds maximum allowed number of items
        """
        if key is None or item is None:
            return None
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.last)
            print("DISCARD: {}".format(self.last))
        self.last = key

    def get(self, key):
        """Returns requested item using provided key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
