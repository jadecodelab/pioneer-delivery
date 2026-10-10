import heapq

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

def assign_drivers(deliveries):
    """
    Assigns every delivery to a driver using the minimum
    possible number of drivers.

    The priority queue stores:
    (driver's current finish time, driver number)
    """
    # sort deliveries in order of start time
    sorted_deliveries = sorted(deliveries, key=lambda delivery:delivery["start"])

    # min heap containing each driver's finish time
    driver_heap = []

    # stores the deliveries assigned to each driver
    driver_schedules = {}

    next_driver_number = 1

    for delivery in sorted_deliveries:
        # reuse the driver who finishes earliest if available
        if(driver_heap and driver_heap[0][0] <= delivery["start"]):
            earliest_finish, driver_number = heapq.heappop(driver_heap)

        # otherwise create a new driver
        else:
            driver_number = next_driver_number
            next_driver_number += 1
            driver_schedules[driver_number] = []

        # assign delivery to selected driver
        driver_schedules[driver_number].append(delivery)

        # add driver's new finish time to the heap
        heapq.heappush(driver_heap, (delivery["finish"], driver_number))

    return driver_schedules
