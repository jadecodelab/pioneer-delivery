import unittest

from closest_pair import closest_pair


class TestClosestPair(unittest.TestCase):
    # Test A1
    def test_a1_two_points(self):
        points = [
            {"id": "A", "x": 0, "y": 0},
            {"id": "B", "x": 3, "y": 4}
        ]

        id1, id2, distance = closest_pair(points)

        self.assertEqual({id1, id2}, {"A", "B"})
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

        id1, id2, distance = closest_pair(points)

        self.assertEqual({id1, id2}, {"C", "D"})
        self.assertEqual(distance, 1)

    # Test A3
    def test_a3_cross_half_pair(self):
        points = [
            {"id": "A", "x": -3, "y": 1},
            {"id": "B", "x": -3, "y": 11},
            {"id": "C", "x": 1, "y": 1},
            {"id": "D", "x": 2, "y": 15}
        ]

        id1, id2, distance = closest_pair(points)

        self.assertEqual({id1, id2}, {"A", "C"})
        self.assertEqual(distance, 16)

    # Test A4
    def test_a4_negative_coordinates(self):
        points = [
            {"id": "A", "x": -5, "y": -5},
            {"id": "B", "x": -5, "y": -2},
            {"id": "C", "x": 6, "y": 8}
        ]

        id1, id2, distance = closest_pair(points)

        self.assertEqual({id1, id2}, {"A", "B"})
        self.assertEqual(distance, 9)

    # Additional test: multiple closest pairs
    def test_multiple_closest_pairs(self):
        points = [
            {"id": "A", "x": 0, "y": 0},
            {"id": "B", "x": 1, "y": 0},
            {"id": "C", "x": 0, "y": 1},
            {"id": "D", "x": 1, "y": 1}
        ]

        id1, id2, distance = closest_pair(points)

        self.assertIn({id1, id2}, [
            {"A", "B"},
            {"A", "C"},
            {"B", "D"},
            {"C", "D"}
        ])
        self.assertEqual(distance, 1)

    # Additional test: invalid input
    def test_requires_at_least_two_points(self):
        with self.assertRaisesRegex(ValueError, "At least two points"):
            closest_pair([{"id": "A", "x": 0, "y": 0}])


if __name__ == "__main__":
    unittest.main(verbosity=2)
