# Pioneer Delivery Algorithm Portfolio

## Project Description

This project implements scheduling algorithms for Pioneer Delivery Company. Pioneer Delivery is a growing local delivery company that receives many delivery requests each day. Each delivery occupies a driver for a specified time interval.

Each delivery has:

- A delivery ID
- A start time
- A finish time

A driver cannot handle overlapping deliveries. However, one delivery may start at the exact time another delivery finishes.

## Programming Language

Python

## Project Organization

```text
pioneer-delivery/
│
├── main.py
├── scheduler.py
├── data.txt
├── test.py
└── README.md
```

## Input File Format and Text Data File

Each delivery is stored on one line using this format: delivery_id start_time finish_time

- The delivery ID is a string.
- Start and finish times are integers.
- The start time must be less than the finish time.

## How to Run the Program

Open a terminal in the project folder and run:

```text
python main.py
```

Run all automated tests with:

```text
python -m unittest -v test.py
```

Expected result:

```text
Ran 18 tests in 0.003s
OK
```

## Task A: Maximum Deliveries for One Driver

### Goal

Find the largest number of deliveries that one driver can complete without overlapping schedules.

### Greedy Algorithm

The program sorts all deliveries by their finish time. It then selects the first delivery and continues selecting a delivery whenever its start time is greater than or equal to the finish time of the previously selected delivery.

The greedy choice is to select the delivery that finishes earliest. This leaves the most available time for the remaining deliveries.

### Running Time

- Sorting takes O(nlogn)
- Scanning the sorted list takes O(n)
- Total running time is O(nlogn)

## Task B: Minimum Number of Drivers

### Goal

Assign every delivery to a driver while using the minimum possible number of drivers.

### Algorithm

The program first sorts deliveries by their start time.
It uses a priority queue implemented with Python's `heapq` module. The priority queue stores each driver's current finish time and driver number.

Deliveries are processed in order of start time. The algorithm checks the driver who finishes earliest.

- If the driver's finish time is less than or equal to the delivery's start time, that driver is reused.
- Otherwise, a new driver is created.

The priority queue always checks the driver who becomes available first. If that driver is still busy when a new delivery starts, then every other driver is also busy. Therefore, creating a new driver is necessary. This guarantees that no unnecessary drivers are created.

### Running Time

- Sorting takes O(nlogn)
- Each delivery is added to or removed from the priority queue in O(logn)
- Total running time is O(nlogn)

## Task C: Minimum Deliveries to Reject

### Relationship to Task A

Task C uses the result from Task A. Task A finds the maximum number of deliveries that one driver can complete without overlapping. Task C then determines how many deliveries cannot be included in that schedule and must be rejected.

### Number of Deliveries Rejected

If there are `n` total deliveries and the maximum number of compatible deliveries is `k`, then: Number rejected = n - k

### Running Time

- Task A takes O(nlogn)
- Total running time is O(nlogn)

## Task D: When a Greedy Choice Fails

Each delivery takes one unit of time. A delivery can only be scheduled at or after its ready time.

The delay for a delivery is: Dj = Tj - Rj

The value of a delivery is: Vj = Pj / (1 + Dj)

The total value of a schedule is the sum of the values of all deliveries.

The proposed greedy strategy processes deliveries in decreasing order of profit. Each delivery is scheduled in the earliest available time slot at or after its ready time.

This strategy does not always produce an optimal schedule.

### Counterexample

| Delivery | Ready Time (Rj) | Profit (Pj) |
| -------- | --------------: | ----------: |
| A        |               0 |           2 |
| B        |               0 |           3 |
| C        |               1 |           1 |

### Schedule Produced by Greedy Strategy

The greedy strategy processes the deliveries in decreasing order of profit: B, A, C

| Delivery | Ready Time | Profit | Scheduled Time | Delay |             Value |
| -------- | ---------: | -----: | -------------: | ----: | ----------------: |
| B        |          0 |      3 |              0 |     0 |   3 / (1 + 0) = 3 |
| A        |          0 |      2 |              1 |     1 |   2 / (1 + 1) = 1 |
| C        |          1 |      1 |              2 |     1 | 1 / (1 + 1) = 0.5 |

Total Value = 3 + 1 + 0.5 = 4.5

### Better Schedule

Consider the following schedule: B, C, A

| Delivery | Ready Time | Profit | Scheduled Time | Delay |             Value |
| -------- | ---------: | -----: | -------------: | ----: | ----------------: |
| B        |          0 |      3 |              0 |     0 |   3 / (1 + 0) = 3 |
| C        |          1 |      1 |              1 |     0 |   1 / (1 + 0) = 1 |
| A        |          0 |      2 |              2 |     2 | 2 / (1 + 2) = 2/3 |

Total Value = 3 + 1 + 2/3 = 4.67

This schedule produces more value than the greedy schedule.

Therefore, the strategy of processing deliveries only in decreasing order of profit does not always produce an optimal schedule.
