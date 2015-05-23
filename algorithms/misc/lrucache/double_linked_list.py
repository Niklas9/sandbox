

class DoubleLinkedList(object):

    items = None
    head = None
    tail = None

    def __init__(self):
        self.items = {}

    def set_head(self, key):
        if key in self.items:  self.delete(key)
        self.items[key] = {'p': None, 'n': self.head}
        if self.head is not None:
            self.items[self.head]['p'] = key
        else:
            self.tail = key
        self.head = key

    def pop(self):
        pop_tail = self.tail
        self.delete(pop_tail)
        return pop_tail

    def delete(self, key):
        if not key in self.items:  return
        next_key = self.items[key]['n']
        prev_key = self.items[key]['p']
        if prev_key in self.items:
            self.items[prev_key]['n'] = next_key
        if next_key in self.items:
            self.items[next_key]['p'] = prev_key
        if self.head == key:
            self.head = next_key
        if self.tail == key:
            self.tail = prev_key
        del self.items[key]
