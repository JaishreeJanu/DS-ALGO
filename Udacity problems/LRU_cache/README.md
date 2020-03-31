## Problem explanation for LRU Cache

Data structure used: **dictionary**.
Two dictionaries: **cache** and **timestamp_cache** have been used.

"cache" stores key-value pairs.
"timestamp-cache" stores key-timestamp pairs. Timestamp corresponding to key is updated if it is being read or it being set in the cache.

### When cache is full and new key-value pair needs to be added

1. In LRU cache, the key which has been not been read or added for longest time, gets deleted from cache.
2. Sort timestamp_cache, get the key (call it "del_key") positioned at **[0]** index.
3. Delete "del_key" and its value from cache and timestamp_cache(Deletes timestamp for this key).
4. Add new key-value pair in cache and timestamp_cache.


### Complexity Analysis

**Time Complexity**: 
- get(key)[To read a key-value pair]: O(1)
- set(key)[If cache already full]: 
Get all timestamp values from timestamp_cache: O(n)
Sort all timestamp values: O(nlogn)
Delete least recently used key from both dictionaries: O(1)

Total Time Complexity for adding new key: O(nlogn)
- If n keys are being added to cache: Time Complexity is O(n<sup>2</sup>logn)


