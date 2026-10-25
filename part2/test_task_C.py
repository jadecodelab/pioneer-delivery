import unittest

from delivery_threshold import select_kth_delivery_time


class TestDeliveryThreshold(unittest.TestCase):

    # Test C1
    def test_c1_fifth_smallest(self):
        delivery_times = [18, 4, 29, 11, 4, 16, 35, 9, 22]

        self.assertEqual(
            select_kth_delivery_time(delivery_times, 5),
            16
        )

    # Test C2
    def test_c2_second_smallest(self):
        delivery_times = [18, 4, 29, 11, 4, 16, 35, 9, 22]

        self.assertEqual(
            select_kth_delivery_time(delivery_times, 2),
            4
        )

    # Test C3
    def test_c3_largest_value(self):
        delivery_times = [18, 4, 29, 11, 4, 16, 35, 9, 22]

        self.assertEqual(
            select_kth_delivery_time(delivery_times, 9),
            35
        )

    # Test C4
    def test_c4_all_duplicate_values(self):
        delivery_times = [7, 7, 7, 7, 7, 7]

        self.assertEqual(
            select_kth_delivery_time(delivery_times, 4),
            7
        )

    # Test C5
    def test_c5_two_values(self):
        self.assertEqual(
            select_kth_delivery_time([8, 3], 1),
            3
        )

    # Test: already sorted input
    def test_sorted_input(self):
        delivery_times = list(range(1, 21))

        self.assertEqual(
            select_kth_delivery_time(delivery_times, 13),
            13
        )

    # Test: reverse sorted input
    def test_reverse_sorted_input(self):
        delivery_times = list(range(20, 0, -1))

        self.assertEqual(
            select_kth_delivery_time(delivery_times, 13),
            13
        )

    # Test: larger input with many duplicates
    def test_larger_input_with_many_duplicates(self):
        delivery_times = [5] * 100 + [1] * 50 + [9] * 50

        self.assertEqual(
            select_kth_delivery_time(delivery_times, 125),
            5
        )



if __name__ == "__main__":
    unittest.main(verbosity=2)

