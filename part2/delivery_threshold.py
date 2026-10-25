def select_kth_delivery_time(delivery_times, k):
    """
    Return the kth-smallest delivery time using 1-based ranking.
    """
    if not 1 <= k <= len(delivery_times):
        raise ValueError("k must be between 1 and the number of delivery times")

    return _select(delivery_times, k)


def _select(values, k):
    """
    Select the kth-smallest value using deterministic median-of-medians.
    """
    # Sorting for small base cases.
    if len(values) <= 5:
        return sorted(values)[k - 1]

    pivot = _choose_pivot(values)

    less = [value for value in values if value < pivot]
    equal = [value for value in values if value == pivot]
    greater = [value for value in values if value > pivot]

    # The desired value is in the values smaller than the pivot.
    if k <= len(less):
        return _select(less, k)

    # The pivot occupies these ranks, including duplicate copies.
    if k <= len(less) + len(equal):
        return pivot

    # Remove the ranks occupied by the less and equal groups.
    new_k = k - len(less) - len(equal)
    return _select(greater, new_k)


def _choose_pivot(values):
    """
    Choose a pivot from the median of medians of groups of at most five.
    """
    medians = []

    for start in range(0, len(values), 5):
        group = sorted(values[start:start + 5])

        # Use the lower median when the final group has an even size.
        median_index = (len(group) - 1) // 2
        medians.append(group[median_index])

    # _select uses a 1-based rank. This chooses the lower median when
    # the number of group medians is even.
    median_rank = (len(medians) + 1) // 2
    return _select(medians, median_rank)


if __name__ == "__main__":
    delivery_times = [18, 4, 29, 11, 4, 16, 35, 9, 22]
    k = 5

    result = select_kth_delivery_time(delivery_times, k)

    print(f"Selected delivery time: {result}")
