
import double_linked_list
import lrucache


class TestLRUCache(object):

    def test_basic_get_set_ops(self):
        lc = lrucache.LRUCache()
        lc.set('a', 1)
        assert lc.get('a') == 1
        lc.set('b', 2)
        lc.set('c', 3)
        assert lc.get('a') is None
        assert lc.get('b') == 2
        assert lc.get('c') == 3


class TestDoubleLinkedList(object):

    def test_set_head(self):
        dll = double_linked_list.DoubleLinkedList()
        dll.set_head('a')
        assert len(dll.items.keys()) == 1
        assert dll.head == 'a'
        assert dll.tail == 'a'

    def test_pop(self):
        dll = double_linked_list.DoubleLinkedList()
        dll.set_head('a')
        assert dll.pop() == 'a'
        assert len(dll.items.keys()) == 0
        assert dll.head is None
        assert dll.tail is None

    def test_pop_several(self):
        dll = double_linked_list.DoubleLinkedList()
        dll.set_head('a')
        dll.set_head('b')
        dll.set_head('c')
        assert dll.pop() == 'a'
        assert dll.pop() == 'b'
        assert dll.pop() == 'c'
        assert len(dll.items.keys()) == 0

    def test_set_head_pop(self):
        dll = double_linked_list.DoubleLinkedList()
        dll.set_head('a')
        dll.set_head('b')
        dll.set_head('a')
        assert dll.pop() == 'b'
        assert dll.pop() == 'a'
        assert len(dll.items.keys()) == 0
