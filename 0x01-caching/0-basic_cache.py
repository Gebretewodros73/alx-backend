#!/usr/bin/python3
""" 0-basic_cache.py """
# Import the BaseCaching class from the parent module
BaseCaching = __import__('base_caching').BaseCaching


# Define the BasicCache class that inherits from BaseCaching
class BasicCache(BaseCaching):
    """ Defines a basic caching system. """

    # Implement the put method
    def put(self, key, item):
        """ Add an item to the cache. """

        # Check if key or item is None
        if key is None or item is None:
            return

        # Assign the item value for the key in the cache
        self.cache_data[key] = item

    # Implement the get method
    def get(self, key):
        """ Retrieve an item from the cache. """

        # Check if key is None or if the key doesn't exist in the cache
        if key is None or key not in self.cache_data:
            return None

        # Return the value linked to the key in the cache
        return self.cache_data[key]
