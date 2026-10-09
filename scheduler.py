def read_deliveries(filename):
    """
    Reads delivery data from a text file.

    Each valid line must contain:
    delivery_id start_time finish_time

    Returns a list of delivery dictionaries.
    """
    deliveries = []

    with open(filename, "r") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line:
                continue

            parts = line.split()

            if(len(parts) != 3):
                raise ValueError(f"Line {line_number} must contain: ID start_time finish_time")

            delivery_id = parts[0]
            start_time = int(parts[1])
            finish_time = int(parts[2])

            if start_time >= finish_time:
                raise ValueError(f"Invalid delivery {delivery_id}")

            deliveries.append({
                "id": delivery_id,
                "start": start_time,
                "finish":finish_time
            })

        return deliveries

def select_max_deliveries(deliveries):
    """
    Selects the maximum number of non-overlapping deliveries.

    The algorithm sorts deliveries by finish time and greedily
    selects the next delivery that starts after the previous one ends.
    """
        
    # sort deliveries by earlies finish time
    sorted_deliveries = sorted(deliveries, key=lambda delivery:delivery["finish"])

    selected = []
    last_finish_time = None

    for delivery in sorted_deliveries:
        # select the first delivery in the list
        if last_finish_time is None:
            selected.append(delivery)
            last_finish_time = delivery["finish"]

        # select the compatibile delivery
        elif delivery["start"] >= last_finish_time:
            selected.append(delivery)
            last_finish_time = delivery["finish"]

    return selected
