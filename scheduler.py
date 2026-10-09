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

