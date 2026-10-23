def count_dispatch_inversions(planned, actual):
    """
    Return the number of delivery-ID pairs whose order in actual
    is reversed from their order in planned.
    """
    # Convert each actual delivery ID into its planned position.
    planned_positions = {
        delivery_id: index
        for index, delivery_id in enumerate(planned)
    }

    actual_ranks = [
        planned_positions[delivery_id]
        for delivery_id in actual
    ]

    _, inversion_count = _sort_and_count(actual_ranks)

    return inversion_count

def _sort_and_count(values):
    """
    Sort values and count inversions using merge sort.
    """
    if len(values) <= 1:
        return values[:], 0

    middle = len(values) // 2

    left, left_count = _sort_and_count(values[:middle])
    right, right_count = _sort_and_count(values[middle:])

    merged, cross_count = _merge_and_count(left, right)

    total_count = left_count + right_count + cross_count

    return merged, total_count

def _merge_and_count(left, right):
    """
    Merge two sorted lists and count cross-half inversions.
    """
    merged = []
    inversion_count = 0

    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])

            # right[right_index] is smaller than every remaining
            # value in the sorted left list.
            inversion_count += len(left) - left_index
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged, inversion_count

if __name__ == "__main__":
    planned = ["D1", "D2", "D3", "D4", "D5"]
    actual = ["D1", "D3", "D4", "D2", "D5"]

    result = count_dispatch_inversions(planned, actual)

    print(f"Number of inversions: {result}")