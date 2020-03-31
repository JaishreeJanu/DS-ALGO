import datetime
import operator

class LRU_Cache(object):

    cache = {}
    timestamp_cache = {}
    capacity = 0
    curr_inc = 0

    def __init__(self, capacity):
        """Initialize class variables
        
        Arguments:
            capacity {int} -- maximun capacity of cache
        """
        self.capacity = capacity

    def get(self, key):
        """Retrieve item from provided key.
        Return -1 if nonexistent
        Arguments:
            key {int} -- Key
        
        Returns:
            [type] -- Return value corresponding to given key
        """
        if key in self.cache:
            self.timestamp_cache[key] = datetime.datetime.now().time()
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        """Set the value if the key is not present in the cache.
        If the cache is at capacity remove the oldest item.
        Arguments:
            key {[type]} -- Key
            value {[type]} -- Value
        """
        if (self.curr_inc < self.capacity):
            self.curr_inc += 1
        else:
            print("Cache is Full, delete least recently used item from cache and add new item ")
            sorted_list = sorted(self.timestamp_cache, key = self.timestamp_cache.get)
            del_key = sorted_list[0]
            del self.cache[del_key]
            del self.timestamp_cache[del_key]
        
        self.cache[key] = value
        self.timestamp_cache[key] = datetime.datetime.now().time()

j_cache = LRU_Cache(6)

print("The value for key 10 is ",j_cache.get(10))
j_cache.set(7,"reichenaustr")
j_cache.set(5,"Bodenseestrasse")
j_cache.set(10,"Donnersbergerbrucke")
j_cache.set(50,"pasing")

print("The value for key 5 is ",j_cache.get(5))
print("The value for key 7 is ",j_cache.get(7))

j_cache.set(100,"Westkreuze")
j_cache.set(120,"Herrsching")

print("The value for key 10 is ",j_cache.get(10))

j_cache.set(20,"Rome")
j_cache.set(30,"Bhutan")
print("The value for key 7 is ",j_cache.get(7))
print("The value for key 30 is ",j_cache.get(30))
print("The value for key 5 is ",j_cache.get(5))

