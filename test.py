import unittest

from scheduler import select_max_deliveries, assign_drivers


def delivery(delivery_id, start, finish):
    return {
        "id": delivery_id,
        "start": start,
        "finish": finish
    }


class TestSelectMaxDeliveries(unittest.TestCase):

    # Test 1: No deliveries
    def test_no_deliveries(self):
        deliveries = []

        result = select_max_deliveries(deliveries)

        self.assertEqual(len(result), 0)

    # Test 2: One delivery
    def test_one_delivery(self):
        deliveries = [
            delivery("D01", 1, 3)
        ]

        result = select_max_deliveries(deliveries)

        self.assertEqual(len(result), 1)

    # Test 3: All deliveries are compatible
    def test_all_compatible(self):
        deliveries = [
            delivery("D01", 1, 3),
            delivery("D02", 3, 5),
            delivery("D03", 5, 7)
        ]

        result = select_max_deliveries(deliveries)

        self.assertEqual(len(result), 3)

    # Test 4: All deliveries overlap
    def test_all_overlapping(self):
        deliveries = [
            delivery("D01", 1, 5),
            delivery("D02", 2, 6),
            delivery("D03", 3, 7)
        ]

        result = select_max_deliveries(deliveries)

        self.assertEqual(len(result), 1)

    # Test 5: The input is not sorted
    def test_unsorted_deliveries(self):
        deliveries = [
            delivery("D01", 5, 7),
            delivery("D02", 1, 3),
            delivery("D03", 3, 5),
            delivery("D04", 2, 4)
        ]

        result = select_max_deliveries(deliveries)

        self.assertEqual(len(result), 3)

    # Test 6: Deliveries share an endpoint
    def test_shared_endpoint(self):
        deliveries = [
            delivery("D01", 1, 4),
            delivery("D02", 2, 4),
            delivery("D03", 4, 6)
        ]

        result = select_max_deliveries(deliveries)

        self.assertEqual(len(result), 2)


class TestAssignDrivers(unittest.TestCase):

    def check_valid_schedules(self, schedules):
        """
        Confirms that no driver has overlapping deliveries.
        """
        for schedule in schedules.values():
            for i in range(len(schedule) - 1):
                current_delivery = schedule[i]
                next_delivery = schedule[i + 1]

                self.assertLessEqual(
                    current_delivery["finish"],
                    next_delivery["start"]
                )

    def test_no_deliveries(self):
        deliveries = []

        result = assign_drivers(deliveries)

        self.assertEqual(len(result), 0)

    def test_one_delivery(self):
        deliveries = [
            delivery("D01", 1, 3)
        ]

        result = assign_drivers(deliveries)

        self.assertEqual(len(result), 1)
        self.check_valid_schedules(result)

    def test_all_compatible(self):
        deliveries = [
            delivery("D01", 1, 3),
            delivery("D02", 3, 5),
            delivery("D03", 5, 7)
        ]

        result = assign_drivers(deliveries)

        self.assertEqual(len(result), 1)
        self.check_valid_schedules(result)

    def test_all_overlapping(self):
        deliveries = [
            delivery("D01", 1, 5),
            delivery("D02", 2, 6),
            delivery("D03", 3, 7)
        ]

        result = assign_drivers(deliveries)

        self.assertEqual(len(result), 3)
        self.check_valid_schedules(result)

    def test_partial_overlap(self):
        deliveries = [
            delivery("D01", 1, 4),
            delivery("D02", 2, 5),
            delivery("D03", 4, 7),
            delivery("D04", 5, 8)
        ]

        result = assign_drivers(deliveries)

        self.assertEqual(len(result), 2)
        self.check_valid_schedules(result)

    def test_unsorted_deliveries(self):
        deliveries = [
            delivery("D01", 5, 8),
            delivery("D02", 1, 4),
            delivery("D03", 2, 5),
            delivery("D04", 4, 6),
            delivery("D05", 6, 9)
        ]

        result = assign_drivers(deliveries)

        self.assertEqual(len(result), 2)
        self.check_valid_schedules(result)


if __name__ == "__main__":
    unittest.main()