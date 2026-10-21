# Calculates the squared Euclidean distance between two points. 
def squared_distance(point1, point2):       
    return (point1["x"] - point2["x"])**2 + (point1["y"] - point2["y"])**2

# Finds the closest pair with brute force method
def brute_force_closest(points):
    if len(points) < 2:
        raise ValueError("Need atleast 2 points")

    closest_pair = None
    smalest_distance = float("inf")

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = squared_distance(points[i],points[j])

            if distance < smalest_distance:
                smalest_distance = distance
                closest_pair = (points[i], points[j])

    return closest_pair[0], closest_pair[1], smalest_distance

if __name__ == "__main__":
    points = [
        {"id": "A", "x": 0, "y": 0},
        {"id": "B", "x": 3, "y": 4}
    ]

    point1, point2, distance = brute_force_closest(points)

    print(f"Closest pair: {point1['id']}, {point2['id']}")
    print(f"Squared distance: {distance}")