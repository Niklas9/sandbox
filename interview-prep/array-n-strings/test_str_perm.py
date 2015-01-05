#!/usr/bin/python

import unittest

import str_perm


m = str_perm.is_perm

class StrPermTest(unittest.TestCase):

    def test_null(self):
        assert m(None, None) == False
        assert m('a', None) == False
        assert m(None, 'a') == False

    def test_random_pos(self):
        assert m('a', 'a') == True
        assert m('ab', 'ba') == True
        assert m('Niklas', 'salkiN') == True
        assert m('qwer', 'wrqe') == True

    def test_random_neg(self):
        assert m('a', 'b') == False
        assert m('Nklas', 'saliN') == False
        assert m('asdf', 'a') == False

if __name__ == '__main__':
    unittest.main()
