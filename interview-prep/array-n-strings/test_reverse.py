#!/usr/bin/python

import unittest

import reverse


m = reverse.reverse

class ReverseTest(unittest.TestCase):

    def test_null(self):
        assert m(None) == None

    def test_random_pos(self):
        assert m('asdf') == 'fdsa'
        assert m('Niklas') == 'salkiN'


if __name__ == '__main__':
    unittest.main()
