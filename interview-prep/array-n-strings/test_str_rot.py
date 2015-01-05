#!/usr/bin/python

import unittest

import str_rot


m = str_rot.is_str_rot

class StrRot(unittest.TestCase):

    def test_random_pos(self):
        assert m('asdf', 'asdf') == True
        assert m('asdf', 'fasd') == True
        assert m('waterbottle', 'erbottlewat') == True

    def test_random_neg(self):
        assert m('asdf', 'a') == False
        assert m('asdf', 'fdsa') == False

if __name__ == '__main__':
    unittest.main()
