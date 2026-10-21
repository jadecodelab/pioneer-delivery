import unittest

from closest_pair import closest_pair


class TestClosestPair(unittest.TestCase):

    def point_ids(self, point1, point2):
        """
        Returns the IDs as a set so the pair can be checked
        without depending on the order.
        """
        return {point1["id"], point2["id"]}

    # Test A1
    def test_a1_two_points(self):
        points = [
            {"id": "A", "x": 0, "y": 0},
            {"id": "B", "x": 3, "y": 4}
        ]

        point1, point2, distance = closest_pair(points)

        self.assertEqual(self.point_ids(point1, point2), {"A", "B"})
        self.assertEqual(distance, 25)

    # Test A2
    def test_a2_closest_pair(self):
        points = [
            {"id": "A", "x": 0, "y": 0},
            {"id": "B", "x": 7, "y": 2},
            {"id": "C", "x": 4, "y": 5},
            {"id": "D", "x": 5, "y": 5},
            {"id": "E", "x": 12, "y": 2},
            {"id": "F", "x": 2, "y": 9}
        ]

        point1, point2, distance = closest_pair(points)

        self.assertEqual(self.point_ids(point1, point2), {"C", "D"})
        self.assertEqual(distance, 1)

    # Test A3
    def test_a3_cross_half_pair(self):
        points = [
            {"id": "A", "x": -3, "y": 1},
            {"id": "B", "x": -3, "y": 11},
            {"id": "C", "x": 1, "y": 1},
            {"id": "D", "x": 2, "y": 15}
        ]

        point1, point2, distance = closest_pair(points)

        self.assertEqual(self.point_ids(point1, point2), {"A", "C"})
        self.assertEqual(distance, 16)

    # Test A4
    def test_a4_negative_coordinates(self):
        points = [
            {"id": "A", "x": -5, "y": -5},
            {"id": "B", "x": -5, "y": -2},
            {"id": "C", "x": 6, "y": 8}
        ]

        point1, point2, distance = closest_pair(points)

        self.assertEqual(self.point_ids(point1, point2), {"A", "B"})
        self.assertEqual(distance, 9)

    # Additional test: multiple closest pairs
    def test_multiple_closest_pairs(self):
        points = [
            {"id": "A", "x": 0, "y": 0},
            {"id": "B", "x": 1, "y": 0},
            {"id": "C", "x": 0, "y": 1},
            {"id": "D", "x": 1, "y": 1}
        ]

        point1, point2, distance = closest_pair(points)

        valid_ids = {"A", "B", "C", "D"}

        self.assertEqual(distance, 1)
        self.assertIn(point1["id"], valid_ids)
        self.assertIn(point2["id"], valid_ids)
        self.assertNotEqual(point1["id"], point2["id"])


if __name__ == "__main__":
    unittest.main(verbosity=2)