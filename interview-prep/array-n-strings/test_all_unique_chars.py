#!/usr/bin/python

import unittest
import string

import all_unique_chars


m = all_unique_chars.is_all_unique

class AllUniqueCharsTest(unittest.TestCase):

    def test_null(self):
        assert m(None) == False

    def test_random_pos(self):
        assert m('asdf') == True
        assert m('asdf uyti') == True
        assert m('asdf ASDF') == True
        assert m('') == True
        assert m(' ') == True
        assert m(string.ascii_letters) == True

    def test_random_neg(self):
        assert m('aaa') == False
        assert m('aba') == False
        assert m('asdf uyti ') == False
        assert m('  ') == False
        assert m(string.ascii_letters * 4) == False

    def test_invalid(self):
        self.assertRaises(all_unique_chars.InvalidInputStringException,
                          m, unichr(257))


if __name__ == '__main__':
    unittest.main()
