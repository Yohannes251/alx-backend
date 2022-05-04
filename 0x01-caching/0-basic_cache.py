#!/usr/bin/env python3
"""
    This module defines a class that is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Implements a caching system that inherits from base_cache"""

    def __init__(self):
        """Initializes the class"""
        BaseCaching.__init__(self)

    def put(self, key, item):
        """Inserts items to cache"""
        if key is None or item is None:
            return None
        self.cache_data[key] = item

    def get(self, key):
        """Returns requested item using provided key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
