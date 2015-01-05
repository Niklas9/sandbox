#!/usr/bin/python

import unittest

import rot_pixels


m = rot_pixels.rot90
p = rot_pixels.Pixel

class RotPixelsTest(unittest.TestCase):

    def test_null(self):
        assert m(None) == None

    def test_random_pos(self):
        assert m([[1]]) == [[1]]
        assert m([[1, 2], [3, 4]]) == [[4, 1], [3, 2]]

    def test_random_neg(self):
        # NOTE(niklas9): test with 3x2 matrix for example, should raise smth
        self.assertRaises(rot_pixels.NotNxNMatrixException, m, [[1, 2], [1]])
        self.assertRaises(rot_pixels.NotNxNMatrixException, m, [[1], [1, 2]])
        self.assertRaises(rot_pixels.NotNxNMatrixException, m,
                          [[1, 2, 3], [1, 2, 3]])
        


if __name__ == '__main__':
    unittest.main()