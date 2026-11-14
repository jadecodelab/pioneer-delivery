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
