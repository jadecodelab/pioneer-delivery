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
- `test.py`: automated unit tests

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
python -m unittest -v test.py
```

The test suite includes:

- Required cases A1 through A4
- A case with multiple tied closest pairs
- Invalid input containing fewer than two points
