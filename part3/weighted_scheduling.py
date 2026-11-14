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

    # Sort deliveries by nondecreasing finish time
    sorted_deliveries = sorted(deliveries, key=lambda delivery: (
        delivery["finish"], delivery["start"], delivery["id"]
    ))

    predecessors = [0]

    for i in range(len(sorted_deliveries)):
        predecessor = find_predecessor(sorted_deliveries, i)
        predecessors.append(predecessor)

    print("Sorted deliveries:")
    print([delivery["id"] for delivery in sorted_deliveries])

    print("Predecessors:")
    print(predecessors)

    return 0, []

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