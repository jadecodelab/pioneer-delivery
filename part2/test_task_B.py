import unittest

from dispatch_inversions import count_dispatch_inversions


class TestDispatchInversions(unittest.TestCase):

    # Test B1
    def test_b1_two_inversions(self):
        planned = ["A", "B", "C", "D", "E"]
        actual = ["A", "C", "D", "B", "E"]

        self.assertEqual(
            count_dispatch_inversions(planned, actual),
            2
        )

    # Test B2
    def test_b2_same_order(self):
        planned = ["A", "B", "C", "D"]
        actual = ["A", "B", "C", "D"]

        self.assertEqual(
            count_dispatch_inversions(planned, actual),
            0
        )

    # Test B3
    def test_b3_reverse_order(self):
        planned = ["A", "B", "C", "D"]
        actual = ["D", "C", "B", "A"]

        self.assertEqual(
            count_dispatch_inversions(planned, actual),
            6
        )

    # Test B4
    def test_b4_one_delivery(self):
        planned = ["A"]
        actual = ["A"]

        self.assertEqual(
            count_dispatch_inversions(planned, actual),
            0
        )

    # Large-count check
    def test_large_reversed_order(self):
        n = 100_000

        planned = list(range(1, n + 1))
        actual = planned[::-1]

        expected = n * (n - 1) // 2

        self.assertEqual(
            count_dispatch_inversions(planned, actual),
            expected
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)