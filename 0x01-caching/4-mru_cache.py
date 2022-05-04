#!/usr/bin/env python3
"""
    This module defines a class that is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Implements MRU caching system that inherits from base_caching"""

    def __init__(self):
        """Initializes the class"""
        BaseCaching.__init__(self)

    def put(self, key, item):
        """Inserts items to cache and removes last inserted element
        if number of elements exceeds maximum allowed number of items
        """
        if key is None or item is None:
            return None

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            recent_key = list(self.cache_data.keys())[-2]
            self.cache_data.pop(recent_key)
            print("DISCARD: {}".format(recent_key))

    def get(self, key):
        """Returns requested item using provided key"""
        if key is None or key not in self.cache_data.keys():
            return None
        reappend_data = self.cache_data.pop(key)
        self.cache_data[key] = reappend_data
        return self.cache_data[key]
