def maximum_profit_with_budget(deliveries, budget):
    """
    Returns:
        maximum_profit: highest possible profit
        selected_ids: selected delivery IDs
        total_fuel: total fuel used
    """
    if budget < 0:
        raise ValueError("Budget cannot be negative")

    dp = [[0] * (budget + 1) for _ in range(len(deliveries) + 1)]

    for i in range(1, len(deliveries) + 1):
        delivery = deliveries[i - 1]
        fuel_cost = delivery["fuel"]
        profit = delivery["profit"]

        for current_budget in range(budget + 1):
            if fuel_cost <= current_budget:
                skip_delivery = dp[i - 1][current_budget]

                select_delivery = (profit + dp[i - 1][current_budget - fuel_cost])

                dp[i][current_budget] = max(skip_delivery, select_delivery)
            else:
                dp[i][current_budget] = dp[i - 1][current_budget]

    selected_ids = []
    total_fuel = 0

    i = len(deliveries)
    current_budget = budget

    while i > 0:
        delivery = deliveries[i - 1]
        fuel_cost = delivery["fuel"]

        if dp[i][current_budget] == dp[i - 1][current_budget]:
            # this delivery was not selected
            i -= 1
        else:
            selected_ids.append(delivery["id"])
            total_fuel += fuel_cost
            current_budget -= fuel_cost
            i -= 1

    selected_ids.reverse()

    return dp[-1][-1], selected_ids, total_fuel

if __name__ == "__main__":
    deliveries = [
        {"id": "P", "fuel": 4, "profit": 20},
        {"id": "Q", "fuel": 3, "profit": 14},
        {"id": "R", "fuel": 5, "profit": 29},
        {"id": "S", "fuel": 2, "profit": 10},
        {"id": "T", "fuel": 6, "profit": 31},
    ]

    budget = 10

    profit, selected_ids, total_fuel = maximum_profit_with_budget(deliveries, budget)

    print("Maximum profit:", profit)
    print("Selected deliveries:", selected_ids)
    print("Total fuel:", total_fuel)

