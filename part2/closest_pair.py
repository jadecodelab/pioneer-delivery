def closest_pair(points):
    """
    Return the IDs of the closest two points and their squared distance.
    """
    if len(points) < 2:
        raise ValueError("At least two points are required")

    # Sort only once. The recursive function preserves both orders.
    points_by_x = sorted(points, key=lambda point: (point["x"], point["y"]))
    points_by_y = sorted(points, key=lambda point: (point["y"], point["x"]))

    point1, point2, distance_squared = _closest_recursive(
        points_by_x,
        points_by_y
    )

    return point1["id"], point2["id"], distance_squared


def _closest_recursive(points_by_x, points_by_y):
    """
    Find the closest pair using divide and conquer.
    """

    # Base case: directly compare groups of two or three points.
    if len(points_by_x) <= 3:
        return _brute_force(points_by_x)

    # Divide the points into left and right halves.
    left_x, right_x, left_y, right_y = _divide_points(
        points_by_x,
        points_by_y
    )

    # Recursively solve each half.
    left_result = _closest_recursive(left_x, left_y)
    right_result = _closest_recursive(right_x, right_y)

    # Start with the better result from the two halves.
    if left_result[2] <= right_result[2]:
        best_result = left_result
    else:
        best_result = right_result

    # Check whether a closer pair crosses the dividing line.
    dividing_x = right_x[0]["x"]

    return _check_strip(
        points_by_y,
        dividing_x,
        best_result
    )


def _divide_points(points_by_x, points_by_y):
    """
    Divide both sorted lists into matching left and right halves.
    """
    middle = len(points_by_x) // 2

    left_x = points_by_x[:middle]
    right_x = points_by_x[middle:]

    # Use IDs because points with the same x-coordinate
    # might be placed in different halves.
    left_ids = {point["id"] for point in left_x}

    left_y = [
        point for point in points_by_y
        if point["id"] in left_ids
    ]

    right_y = [
        point for point in points_by_y
        if point["id"] not in left_ids
    ]

    return left_x, right_x, left_y, right_y


def _check_strip(points_by_y, dividing_x, best_result):
    """
    Check for a closer pair crossing the dividing line.
    """
    point1, point2, best_distance = best_result

    # Keep only points close enough to the dividing line.
    strip = [
        point
        for point in points_by_y
        if (point["x"] - dividing_x) ** 2 < best_distance
    ]

    # The strip is already sorted by y-coordinate.
    for i in range(len(strip)):

        # Only the next seven points can possibly be closer.
        for j in range(i + 1, min(i + 8, len(strip))):
            y_difference = strip[j]["y"] - strip[i]["y"]

            # Later points will have an even larger y-difference.
            if y_difference**2 >= best_distance:
                break

            distance = _squared_distance(strip[i], strip[j])

            if distance < best_distance:
                point1 = strip[i]
                point2 = strip[j]
                best_distance = distance

    return point1, point2, best_distance


def _brute_force(points):
    """
    Compare every pair in a small group.
    """
    best_pair = None
    best_distance = float("inf")

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = _squared_distance(points[i], points[j])

            if distance < best_distance:
                best_pair = (points[i], points[j])
                best_distance = distance

    return best_pair[0], best_pair[1], best_distance


def _squared_distance(point1, point2):
    """
    Calculate squared Euclidean distance.
    """
    x_difference = point1["x"] - point2["x"]
    y_difference = point1["y"] - point2["y"]

    return x_difference**2 + y_difference**2


if __name__ == "__main__":
    points = [
        {"id": "A", "x": 0, "y": 0},
        {"id": "B", "x": 7, "y": 2},
        {"id": "C", "x": 4, "y": 5},
        {"id": "D", "x": 5, "y": 5},
        {"id": "E", "x": 12, "y": 2},
        {"id": "F", "x": 2, "y": 9}
    ]

    id1, id2, distance_squared = closest_pair(points)

    print(f"Closest pair: {id1} and {id2}")
    print(f"Squared distance: {distance_squared}")