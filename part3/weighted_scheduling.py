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

    print(sorted_deliveries)

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