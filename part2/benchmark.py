import random
import statistics
import time

from closest_pair import closest_pair
from dispatch_inversions import count_dispatch_inversions
from delivery_threshold import select_kth_delivery_time


def measure(function, *arguments, repeats=3):
    """
    Returns the median execution time in milliseconds.
    """
    times = []

    for _ in range(repeats):
        start_time = time.perf_counter()
        function(*arguments)
        end_time = time.perf_counter()

        times.append((end_time - start_time) * 1000)

    return statistics.median(times)


def create_points(n):
    """
    Creates n points with unique x-coordinates.
    """
    random_generator = random.Random(42)

    points = [
        {
            "id": f"P{i}",
            "x": i,
            "y": random_generator.randint(-1_000_000, 1_000_000)
        }
        for i in range(n)
    ]

    random_generator.shuffle(points)

    return points


def create_dispatch_orders(n):
    """
    Creates a planned order and a completely reversed actual order.
    """
    planned = list(range(n))
    actual = planned[::-1]

    return planned, actual


def create_delivery_times(n):
    """
    Creates delivery times with duplicate values.
    """
    random_generator = random.Random(42)

    return [
        random_generator.randint(0, n)
        for _ in range(n)
    ]


def main():
    input_sizes = [100, 1000, 5000]

    print("Performance Results")
    print("-" * 70)
    print(
        f"{'n':<10}"
        f"{'Task A (ms)':<18}"
        f"{'Task B (ms)':<18}"
        f"{'Task C (ms)':<18}"
    )
    print("-" * 70)

    for n in input_sizes:
        points = create_points(n)
        planned, actual = create_dispatch_orders(n)
        delivery_times = create_delivery_times(n)
        k = (n + 1) // 2

        task_a_time = measure(
            closest_pair,
            points
        )

        task_b_time = measure(
            count_dispatch_inversions,
            planned,
            actual
        )

        task_c_time = measure(
            select_kth_delivery_time,
            delivery_times,
            k
        )

        print(
            f"{n:<10}"
            f"{task_a_time:<18.3f}"
            f"{task_b_time:<18.3f}"
            f"{task_c_time:<18.3f}"
        )


if __name__ == "__main__":
    main()