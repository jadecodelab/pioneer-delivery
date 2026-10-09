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

## Project Files

```text
pioneer-delivery/
│
├── main.py
├── scheduler.py
├── data.txt
└── README.md
```

## Task A: Maximum Deliveries for One Driver

### Goal:

Find the largest number of deliveries that one driver can complete without overlapping schedules.

### Algorithm:

The program sorts all deliveries by their finish time. It then selects the first delivery and continues selecting a delivery whenever its start time is greater than or equal to the finish time of the previously selected delivery.
The greedy choice is to select the delivery that finishes earliest. This leaves the most available time for the remaining deliveries.

### Running Time:

- Sorting takes O(nlogn)
- Scanning the sorted list takes O(n)
- Total running time is O(nlogn)
