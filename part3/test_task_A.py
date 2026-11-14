import unittest

from weighted_scheduling import maximum_profit_schedule


class TestWeightedScheduling(unittest.TestCase):

    def test_assignment_example(self):
        deliveries = [
            {"id": "A", "start": 0, "finish": 3, "profit": 50},
            {"id": "B", "start": 1, "finish": 4, "profit": 60},
            {"id": "C", "start": 3, "finish": 5, "profit": 40},
            {"id": "D", "start": 4, "finish": 7, "profit": 70},
            {"id": "E", "start": 5, "finish": 8, "profit": 50},
            {"id": "F", "start": 7, "finish": 9, "profit": 50},
        ]

        profit, selected_ids = maximum_profit_schedule(deliveries)

        self.assertEqual(profit, 180)
        self.assertEqual(selected_ids, ["B", "D", "F"])

    def test_empty_delivery_list(self):
        profit, selected_ids = maximum_profit_schedule([])

        self.assertEqual(profit, 0)
        self.assertEqual(selected_ids, [])

    def test_deliveries_touch_at_endpoint(self):
        deliveries = [
            {"id": "A", "start": 0, "finish": 2, "profit": 10},
            {"id": "B", "start": 2, "finish": 4, "profit": 20},
        ]

        profit, selected_ids = maximum_profit_schedule(deliveries)

        self.assertEqual(profit, 30)
        self.assertEqual(selected_ids, ["A", "B"])

    def test_overlapping_deliveries(self):
        deliveries = [
            {"id": "A", "start": 0, "finish": 5, "profit": 100},
            {"id": "B", "start": 1, "finish": 2, "profit": 40},
            {"id": "C", "start": 2, "finish": 4, "profit": 40},
            {"id": "D", "start": 4, "finish": 6, "profit": 40},
        ]

        profit, selected_ids = maximum_profit_schedule(deliveries)

        self.assertEqual(profit, 120)
        self.assertEqual(selected_ids, ["B", "C", "D"])


if __name__ == "__main__":
    unittest.main()