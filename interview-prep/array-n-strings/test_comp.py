#!/usr/bin/python

import unittest

import comp

m = comp.comp
im = comp.decomp 

class CompTest(unittest.TestCase):

    def test_null(self):
        assert im(None) == m(None) == None

    def test_random_pos(self):
        assert m('a') == 'a'
        assert m('abc') == 'abc'
        assert m('aa') == 'aa'
        assert m('aab') == 'aab'
        assert m('aaab') == 'a3b'
        assert m('aabb') == 'aabb'
        assert m('aabbb') == 'a2b3'
        assert m('aabbccdd') == 'aabbccdd'  # only return c if it's smaller
        assert m('aaaaaabbcccdddd') == 'a6b2c3d4'
        assert im('a') == 'a'
        assert im('abc') == 'abc'
        assert im('a2') == 'aa'
        assert im('a6b2c3d4') == 'aaaaaabbcccdddd'

    def test_random_neg(self):
        assert im('3') == None


if __name__ == '__main__':
    unittest.main()