# Pioneer Delivery Algorithm Portfolio Part II

## Programming Language and Dependencies

- Python 3
- No third-party packages are required

# Task A: Closest Delivery Locations

## Goal

Task A finds the two delivery locations that are geographically closest to
each other using a divide-and-conquer algorithm.

## Input Format

The `closest_pair` function accepts a list of location dictionaries. Each
location contains a unique ID, an integer x-coordinate, and an integer
y-coordinate.

```python
points = [
    {"id": "A", "x": 0, "y": 0},
    {"id": "B", "x": 3, "y": 4}
]
```

Input assumptions:

- There are at least two locations.
- Every location ID is unique.
- Coordinates are integers.
- No two locations have identical coordinates.

If fewer than two locations are provided, the function raises a `ValueError`.

## Output Format

The function returns:

```text
(first_id, second_id, squared_distance)
```

For the example above, the result is:

```text
("A", "B", 25)
```

If multiple pairs have the same minimum distance, any one of those pairs is
acceptable.

## Algorithm

The program uses the divide-and-conquer closest-pair algorithm.

1. Sort all points once by x-coordinate and once by y-coordinate.
2. Divide the x-sorted points into left and right halves.
3. Divide the y-sorted points into the same halves using their unique IDs.
4. Recursively find the closest pair in each half.
5. Keep the better result from the two halves.
6. Build a vertical strip around the dividing line.
7. Preserve the strip points in their existing y-coordinate order.
8. Compare each strip point with at most the next seven points.
9. Return the IDs of the closest pair and their squared distance.

Maintaining the y-sorted order through recursion avoids sorting at every
recursive level.

## Complexity

- Time complexity: `O(n log n)`

## Files

- `closest_pair.py`: Task A implementation and demonstration input
- `test_task_A.py`: Task A automated unit tests

## Running the Program

Open a terminal in the project directory and run:

```text
cd part2
python closest_pair.py
```

Expected demonstration output:

```text
Closest pair: C and D
Squared distance: 1
```

## Running the Tests

After changing to the `part2` directory, run:

```text
python -m unittest -v test_task_A.py
```

The test suite includes:

- Required cases A1 through A4
- A case with multiple tied closest pairs
- Invalid input containing fewer than two points

# Task B: Counting Dispatch-Order Inversions

## Goal

Task B counts how many pairs of delivery IDs appear in the opposite order in
the actual dispatch sequence compared with the planned sequence. Each reversed
pair is called an inversion.

## Input Format

The `count_dispatch_inversions` function accepts two lists containing delivery
IDs:

```python
planned = ["D1", "D2", "D3", "D4", "D5"]
actual = ["D1", "D3", "D4", "D2", "D5"]
```

The implementation assumes valid input:

- Both lists have the same length and contain at least one ID.
- Both lists contain the same delivery IDs.
- Every delivery ID appears exactly once in each list.

## Output Format

The function returns the total number of inversions as an integer. For the
example above, the result is: `2`

The inverted pairs are `(D2, D3)` and `(D2, D4)` because `D2` was planned
before both IDs but appears after them in the actual order.

## Algorithm

The program uses a merge-sort-based inversion-counting algorithm.

1. Store the planned position of every delivery ID in a dictionary.
2. Replace each ID in the actual sequence with its planned position.
3. Recursively divide the resulting rank array into left and right halves.
4. Sort and count inversions inside each half.
5. Merge the two sorted halves while counting cross-half inversions.
6. When a right-half value is smaller than the current left-half value, add
   the number of values remaining in the left half.
7. Return the sum of the left, right, and cross-half inversion counts.

For the example input, the actual sequence becomes:

```text
[0, 2, 3, 1, 4]
```

The values `2` and `3` both form an inversion with `1`, giving a total of `2`.

## Complexity

- Time complexity: `O(n log n)`

Python integers can represent the required large-count case. A reversed input
of 100,000 IDs produces `4,999,950,000` inversions.

## Files

- `dispatch_inversions.py`: Task B implementation and demonstration input
- `test_task_B.py`: Task B automated unit tests

## Running the Program

After changing to the `part2` directory, run:

```text
python dispatch_inversions.py
```

Expected demonstration output:

```text
Number of inversions: 2
```

## Running the Tests

Run the Task B tests with:

```text
python -m unittest -v test_task_B.py
```

The test suite includes all required cases B1 through B4:

- Two inversions
- Identical planned and actual orders
- Completely reversed order
- A single delivery ID

Run all Task A and Task B tests with:

```text
python -m unittest discover -v
```
