'''
LRU Cache: Design an build a "least recently used" cache, which evicts the least recently used item. The cache should map
from keys to values (allowing you to insert and retrieve a value associated with a particular key) and be initialized with a max size. 
When it is full, it should evict the least recently used item.
'''

class LRUCache(object):

	def __init__(self, max_size):
		self.max = max_size
		self.size = 0
		self.cache = {}
		self.ordering = []

	def add(self, key, value):
		if key in self.cache:
			self.cache[key].append(value)
		else:
			self.cache[key] = [value]
	
		self.size += 1
		self.ordering.append((key, value))

		if self.size > self.max:
			key, value = self.ordering.pop(0)
			if len(self.cache[key]) == 1:
				del self.cache[key]
			else:
				self.cache[key].remove(value)
			self.size -= 1


cache = LRUCache(5)
cache.add("fruit", "apple")
cache.add("fruit", "orange")
cache.add("fruit", "banana")
cache.add("vegetable", "cucumber")
cache.add("meat", "chicken")
print(cache.cache)
cache.add("meat", "beef")
print(cache.cache)
cache.add("fruit", "grapefruit")
print(cache.cache)