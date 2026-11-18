def find_predecessor(sorted_deliveries, delivery_index):
    """
    Finds the number of the last delivery that is compatible
    with the delivery at delivery_index.

    Returns 0 if no compatible delivery exists.
    """

    current_delivery = sorted_deliveries[delivery_index]
    start_time = current_delivery["start"]

    low = 0
    high = delivery_index - 1
    predecessor = 0

    while low <= high:
        middle = (low + high) // 2

        if sorted_deliveries[middle]["finish"] <= start_time:
            # this delivery is compatible. Save it and continue searching
            # p(i) is 1-based: list index middle is delivery number middle + 1
            # (0 is reserved for "no compatible delivery")
            predecessor = middle + 1
            low = middle + 1
        else:
            high = middle - 1

    return predecessor

def maximum_profit_schedule(deliveries):
    """
    Returns:
        maximum_profit: the highest possible total profit
        selected_ids: IDs of the selected deliveries in chronological order
    """
    if not deliveries:
        return 0, []

    # Sort deliveries by nondecreasing finish time
    sorted_deliveries = sorted(deliveries, key=lambda delivery: (
        delivery["finish"], delivery["start"], delivery["id"]
    ))

    # predecessors[0] is an unused placeholder so that predecessors[i] lines up with dp[i]
    predecessors = [0]

    for i in range(len(sorted_deliveries)):
        predecessor = find_predecessor(sorted_deliveries, i)
        predecessors.append(predecessor)

    # DP[0] means no deliveries have been considered.
    dp = [0] * (len(sorted_deliveries) + 1)

    for i in range(1, len(sorted_deliveries) + 1):
        current_delivery = sorted_deliveries[i - 1]

        skip_current = dp[i - 1]

        select_current = (current_delivery["profit"] + dp[predecessors[i]])

        dp[i] = max(skip_current, select_current)

    selected_ids = []
    i = len(sorted_deliveries)

    while i > 0:
        if dp[i] == dp[i - 1]:
            # current delivery was skipped
            i -= 1
        else:
            selected_ids.append(sorted_deliveries[i - 1]["id"])
            i = predecessors[i]

    # we reconstructed backward, so reverse the ids
    selected_ids.reverse()

    return dp[-1], selected_ids


if __name__ == "__main__":
    deliveries = [
        {"id": "A", "start": 0, "finish": 3, "profit": 50},
        {"id": "B", "start": 1, "finish": 4, "profit": 60},
        {"id": "C", "start": 3, "finish": 5, "profit": 40},
        {"id": "D", "start": 4, "finish": 7, "profit": 70},
        {"id": "E", "start": 5, "finish": 8, "profit": 50},
        {"id": "F", "start": 7, "finish": 9, "profit": 50},
    ]

    profit, selected_ids = maximum_profit_schedule(deliveries)

    print("Maximum profit:", profit)
    print("Selected deliveries:", selected_ids)