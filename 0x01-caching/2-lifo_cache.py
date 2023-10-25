#!/usr/bin/env python3

"""
LIFOCache Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching.
    """
    def put(self, key, item):
        """
        Add an item to the cache.
        
        Args:
            key (str): The key to be added.
            item (str): The item to be cached.
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = list(self.cache_data.keys())[-1]
                print(f'DISCARD: {removed}')
                del self.cache_data[removed]
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.
        
        Args:
            key (str): The key of the item to retrieve.
            
        Returns:
            str: The cached item.
        """
        return self.cache_data.get(key, None)
