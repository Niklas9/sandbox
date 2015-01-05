#!/usr/bin/python

import unittest

import zrc


m = zrc.zrc

class ZrcTest(unittest.TestCase):

    def test_null(self):
        assert m(None) == None

    def test_random_pos(self):
        assert m([[1]]) == [[1]]
        assert m([[1, 0], [2, 3]]) == [[0, 0], [2, 0]]
        assert (m([[1, 2, 3], [4, 0, 5], [3, 2, 1]]) ==
                  [[1, 0, 3], [0, 0, 0], [3, 0, 1]])
        in1 = [[1, 2, 0],
               [4, 5, 6],
               [0, 7, 8]]
        out1 = [[0, 0, 0],
                [0, 5, 0],
                [0, 0, 0]]
        assert m(in1) == out1

    def test_random_neg(self):
        # TODO(niklas9):
        # * a neg here could be an array of size M with different length of
        #   second level arrays (N varies)
        pass

if __name__ == '__main__':
    unittest.main()
