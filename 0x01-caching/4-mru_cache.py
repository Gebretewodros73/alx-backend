#!/usr/bin/env python3

"""
MRUCache Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching.
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key (str): The key to be added.
            item (str): The item to be cached.
        """
        if key and item:
            if key in self.cache_data:
                del self.cache_data[key]
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = max(self.cache_data, key=self.cache_data.get)
                del self.cache_data[removed]
                print(f'DISCARD: {removed}')
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            str: The cached item.
        """
        if key in self.cache_data:
            del self.cache_data[key]
            self.cache_data[key] = key
        return self.cache_data.get(key, None)
