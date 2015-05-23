
import double_linked_list


class LRUCache(object):

    def __init__(self):
        self.dll = double_linked_list.DoubleLinkedList()
        self.cache = {}
        self.cache_counter = 0
        self.cache_limit = 2

    def set(self, k, v):
        self.cache[k] = v
        self.dll.set_head(k)
        self.cache_counter += 1
        if self.cache_counter == self.cache_limit:
            del self.cache[self.dll.pop()]

    def get(self, k):
        if not k in self.cache:  return None
        self.dll.set_head(k)
        return self.cache[k]
