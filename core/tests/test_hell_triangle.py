from unittest import TestCase, main
from core.impl.hell_triangle import HellTriangle


class TestHellTriangle(TestCase):
    def setUp(self):
        self.triangles = {
            1: [[1]],
            8: [[6], [1,2]],
            15: [[6], [1,2], [5, 7, 3]],
            24: [[6], [1,2], [5, 7, 3], [8, 3, 9, 9]],
            26: [[6], [3, 5], [9, 7, 1], [4, 6, 8, 4]]
        }

    def test_hell_triangle(self):
        for expected, triangle in self.triangles.items():
            with self.subTest():
                ht = HellTriangle(triangle)
                self.assertEqual(expected, ht.find_max_sum())

    def test_hell_triangle_expection(self):
        self.assertEqual(AssertionError, HellTriangle(None))

if __name__ == '__main__':
    main()
