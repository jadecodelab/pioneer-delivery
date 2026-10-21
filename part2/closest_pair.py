# Calculates the squared Euclidean distance between two points. 
def squared_distance(point1, point2):       
    return (point1["x"] - point2["x"])**2 + (point1["y"] - point2["y"])**2

# Finds the closest pair with brute force method
def brute_force_closest(points):
    if len(points) < 2:
        raise ValueError("At least two points are required")

    closest_pair = None
    smallest_distance = float("inf")

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = squared_distance(points[i],points[j])

            if distance < smallest_distance:
                smallest_distance = distance
                closest_pair = (points[i], points[j])

    return closest_pair[0], closest_pair[1], smallest_distance


def sorted_points(points):
    """
    Creates two sorted versions of the points:
    - Sorted by x-coordinate for dividing the points
    - Sorted by y-coordinate for checking the strip
    """
    if len(points) < 2:
        raise ValueError("At least two points are required")

    sorted_by_x = sorted(points, key=lambda point: (point["x"]))
    sorted_by_y = sorted(points, key=lambda point:(point["y"]))

    return sorted_by_x, sorted_by_y

def divide_points(sorted_by_x, sorted_by_y):
    mid = len(sorted_by_x) // 2

    left_by_x = sorted_by_x[:mid]
    right_by_x = sorted_by_x[mid:]

    left_ids = {point["id"] for point in left_by_x}

    left_by_y = [point for point in sorted_by_y if point["id"] in left_ids]
    right_by_y = [point for point in sorted_by_y if point["id"] not in left_ids]

    return left_by_x, right_by_x, left_by_y, right_by_y


def closest_pair_recursive(sorted_by_x, sorted_by_y):
    """
    Recursively finds the closest pair inside the current set of points.

    The strip check will be added in the next step.
    """

    # For small sets, compare every pair directly
    if len(sorted_by_x) <= 3:
        return brute_force_closest(sorted_by_x)

    # Divide the points into left and right halves
    left_by_x, right_by_x, left_by_y, right_by_y = divide_points(sorted_by_x, sorted_by_y)

    # Recursively find the closest pair in each half
    left_result = closest_pair_recursive(left_by_x, left_by_y)
    right_result = closest_pair_recursive(right_by_x, right_by_y)

    # Check whether a closer pair crosses the dividing line
    return check_strip(
        sorted_by_x,
        sorted_by_y,
        left_result,
        right_result
    )

    return right_result

def closest_pair(points):
    """
    Starts the divide-and-conquer closest-pair algorithm.
    """
    sorted_by_x, sorted_by_y = sorted_points(points)

    return closest_pair_recursive(sorted_by_x, sorted_by_y)

def check_strip(sorted_by_x, sorted_by_y, left_result, right_result):
    """
    Checks whether a closer pair crosses the dividing line.

    The points in the strip are already sorted by y-coordinate.
    """

    # Start with the better pair found in the two halves
    if left_result[2] <= right_result[2]:
        point1, point2, best_distance = left_result
    else:
        point1, point2, best_distance = right_result

    # Use the first point in the right half as the dividing x-coordinate
    middle = len(sorted_by_x) // 2
    dividing_x = sorted_by_x[middle]["x"]

    # Keep only points within the current best distance
    strip = [
        point
        for point in sorted_by_y
        if (point["x"] - dividing_x) ** 2 < best_distance
    ]

    # Compare each point with nearby points in y-order
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 8, len(strip))):
            y_difference = strip[j]["y"] - strip[i]["y"]

            # If the y-distance is already too large,
            # later points will also be too far away
            if y_difference ** 2 >= best_distance:
                break

            distance = squared_distance(strip[i], strip[j])

            if distance < best_distance:
                point1 = strip[i]
                point2 = strip[j]
                best_distance = distance

    return point1, point2, best_distance

if __name__ == "__main__":
    points = [
        {"id": "A", "x": 0, "y": 0},
        {"id": "B", "x": 7, "y": 2},
        {"id": "C", "x": 4, "y": 5},
        {"id": "D", "x": 5, "y": 5},
        {"id": "E", "x": 12, "y": 2},
        {"id": "F", "x": 2, "y": 9}
    ]

    points_by_x, points_by_y = sorted_points(points)

    left_by_x, right_by_x, left_by_y, right_by_y = divide_points(
        points_by_x,
        points_by_y
    )

    print("Sorted by x:")
    print([point["id"] for point in points_by_x])

    print("\nSorted by y:")
    print([point["id"] for point in points_by_y])

    print("\nLeft half:")
    print([point["id"] for point in left_by_x])

    print("\nRight half:")
    print([point["id"] for point in right_by_x])

    point1, point2, distance = closest_pair(points)

    print("\nClosest pair found inside the halves:")
    print(f"{point1['id']} and {point2['id']}")
    print(f"Squared distance: {distance}")