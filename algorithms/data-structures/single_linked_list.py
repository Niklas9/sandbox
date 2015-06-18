

class Node(object):

    next = None
    value = None

    def __init__(self, next, value):
        self.next = next
        self.value = value


c = Node(None, 'c')
b = Node(c, 'b')
a = Node(b, 'a')

def reverse(head):
    prev = None
    current = head
    while not current is None:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp

reverse(a)

t = c
while t is not None:
    print t.value
    t = t.next
