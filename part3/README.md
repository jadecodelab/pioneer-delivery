## Task A: Maximum-Profit Delivery Scheduling

### Purpose

Task A selects a set of non-overlapping deliveries that produces the maximum total profit. A delivery is represented by its ID, start time, finish time, and profit.

Deliveries that finish at the exact time another delivery starts are compatible.

### Input Format

Each delivery is represented as a dictionary:

```python
{
    "id": "A",
    "start": 0,
    "finish": 3,
    "profit": 50
}
```

### Output Format

The function returns:
maximum profit,
selected delivery IDs in chronological order

### Algorithm

The algorithm uses weighted interval scheduling with dynamic programming.

1. Sort the deliveries by finish time.
2. For each delivery, find its latest compatible predecessor using binary search.
3. Build a DP table.
4. For each delivery, compare:
   - Skipping the delivery
   - Selecting the delivery and adding the best compatible profit
5. Trace backward through the DP table to recover the selected delivery IDs.

The recurrence is: DP[i] = max(DP[i - 1], profit[i] + DP[p(i)])

p(i) is the last delivery compatible with delivery i

### Complexity

The sorting and predecessor calculations take O(n log n) time.

The DP table, predecessor list, and schedule reconstruction use O(n) additional space.

### Running the Program

From the part3 folder, run:

```python
python weighted_scheduling.py
```

### Running the Tests

```python
python -m unittest -v test_task_A.py
```

The test suite contains four tests:

- The assignment example
- Empty delivery input
- Deliveries touching at an endpoint
- Overlapping deliveries

## Task B: Delivery Selection with a Fuel Budget

### Purpose

Task B selects deliveries with the maximum total profit while staying within a limited fuel budget. Each delivery can be selected at most once.

This is the 0/1 knapsack problem.

### Input Format

Each delivery is represented as:

```python
{
    "id": "P",
    "fuel": 4,
    "profit": 20
}
```

### Output Format

```
maximum profit
selected delivery IDs
total fuel used
```

### Algorithm

The algorithm uses a two-dimensional bottom-up DP table.

DP[i][b] represents the maximum profit obtainable using the first i deliveries with a fuel budget of b.

For each delivery, the algorithm compares:

- Skipping the delivery
- Selecting the delivery, if enough fuel is available

The recurrence is:
DP[i][b] = max(
DP[i - 1][b],
profit[i] + DP[i - 1]b - fuel[i]]
)

The previous row is used when selecting a delivery, so no delivery can be selected more than once.

After filling the table, the algorithm works backward through it to recover the selected delivery IDs and total fuel used.

### Complexity

Time: O(nB)

Space: O(nB)

n is the number of deliveries and B is the numerical fuel budget.

### Running the Program

From the part3 folder, run:

```python
python knapsack.py
```

### Running the Tests

```python
python -m unittest -v test_task_B.py
```

The test suite includes:

- The assignment example
- Zero fuel budget
- An item that exactly fits the budget
- Empty delivery input
- An independent brute-force comparison for a small input

## Task C: Event Log Cleanup

### Purpose

Task C removes the maximum number of allowed characters from an event-log string while keeping a required pattern as a subsequence.

A subsequence keeps characters in the same order, but the characters do not need to be next to each other.

### Input Format

The function receives:

```python
source = "abbaa"
pattern = "aba"
target_indices = [0, 1, 2]
```

### Output

maximum number of removals

original indices that were removed

### Algorithm

The algorithm uses a two-dimensional bottom-up DP table.

DP[i][j] represents the maximum number of deletions after processing the first i characters of source while matching the first j characters of pattern.

For each source character, the algorithm considers three choices:

1. Keep the character without matching it.
2. Delete it if its original index is in target_indices.
3. Keep it to match the next character in pattern.
   Impossible partial matches are represented using negative infinity.

After filling the table, the algorithm works backward from DP[n][m] to recover the original indices that were deleted.

### Complexity

Time: O(nm)

Space: O(nm)

n is the length of source
m is the length of pattern

### Running the Program

From the part3 folder, run:

```python
python event_log_cleanup.py
```

### Running the Tests

```python
python -m unittest -v test_task_C.py
```

The test suite includes:

- The four assignment examples
- No allowed deletions
- Repeated characters
- Verification that the pattern remains a subsequence
