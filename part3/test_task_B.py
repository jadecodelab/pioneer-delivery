from itertools import combinations
import unittest

from knapsack import maximum_profit_with_budget

def brute_force_best_profit(deliveries, budget):
    best_profit = 0

    for number_selected in range(len(deliveries) + 1):
        for combination in combinations(deliveries, number_selected):
            total_fuel = sum(
                delivery["fuel"] for delivery in combination
            )

            total_profit = sum(
                delivery["profit"] for delivery in combination
            )

            if total_fuel <= budget:
                best_profit = max(best_profit, total_profit)

    return best_profit

class TestKnapsack(unittest.TestCase):

    def test_assignment_example(self):
        deliveries = [
            {"id": "P", "fuel": 4, "profit": 20},
            {"id": "Q", "fuel": 3, "profit": 14},
            {"id": "R", "fuel": 5, "profit": 29},
            {"id": "S", "fuel": 2, "profit": 10},
            {"id": "T", "fuel": 6, "profit": 31},
        ]

        profit, selected_ids, total_fuel = (
            maximum_profit_with_budget(deliveries, 10)
        )

        self.assertEqual(profit, 53)
        self.assertEqual(selected_ids, ["Q", "R", "S"])
        self.assertEqual(total_fuel, 10)

    def test_zero_budget(self):
        deliveries = [
            {"id": "A", "fuel": 2, "profit": 10},
            {"id": "B", "fuel": 3, "profit": 20},
        ]

        profit, selected_ids, total_fuel = (
            maximum_profit_with_budget(deliveries, 0)
        )

        self.assertEqual(profit, 0)
        self.assertEqual(selected_ids, [])
        self.assertEqual(total_fuel, 0)

    def test_item_exactly_fits_budget(self):
        deliveries = [
            {"id": "A", "fuel": 5, "profit": 25},
            {"id": "B", "fuel": 6, "profit": 30},
        ]

        profit, selected_ids, total_fuel = (
            maximum_profit_with_budget(deliveries, 5)
        )

        self.assertEqual(profit, 25)
        self.assertEqual(selected_ids, ["A"])
        self.assertEqual(total_fuel, 5)

    def test_empty_delivery_list(self):
        profit, selected_ids, total_fuel = (
            maximum_profit_with_budget([], 10)
        )

        self.assertEqual(profit, 0)
        self.assertEqual(selected_ids, [])
        self.assertEqual(total_fuel, 0)

    def test_dp_matches_brute_force(self):
        deliveries = [
            {"id": "A", "fuel": 2, "profit": 8},
            {"id": "B", "fuel": 3, "profit": 12},
            {"id": "C", "fuel": 4, "profit": 15},
        ]

        budget = 5

        expected_profit = brute_force_best_profit(
            deliveries,
            budget
        )

        actual_profit, selected_ids, total_fuel = (
            maximum_profit_with_budget(deliveries, budget)
        )

        self.assertEqual(actual_profit, expected_profit)
        self.assertLessEqual(total_fuel, budget)   

if __name__ == "__main__":
    unittest.main()