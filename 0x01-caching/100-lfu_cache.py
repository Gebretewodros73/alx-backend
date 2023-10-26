#!/usr/bin/env python3

"""
LFUCache Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching.
    """
    def __init__(self):
        super().__init__()
        self.usage_count = {}

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key (str): The key to be added.
            item (str): The item to be cached.
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = min(self.usage_count, key=self.usage_count.get)
                del self.usage_count[removed]
                del self.cache_data[removed]
                print(f'DISCARD: {removed}')
            self.cache_data[key] = item
            self.usage_count[key] = 0

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            str: The cached item.
        """
        if key in self.cache_data:
            self.usage_count[key] += 1
            return self.cache_data[key]
        return None
