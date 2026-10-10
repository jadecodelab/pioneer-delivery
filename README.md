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

## Task B: Minimum Number of Drivers

### Goal:

Assign every delivery to a driver while using the minimum possible number of drivers.

### Algorithm:

The program first sorts deliveries by their start time.
It uses a priority queue implemented with Python's `heapq` module. The priority queue stores each driver's current finish time and driver number.

Deliveries are processed in order of start time. The algorithm checks the driver who finishes earliest.

- If the driver's finish time is less than or equal to the delivery's start time, that driver is reused.
- Otherwise, a new driver is created.

The priority queue always checks the driver who becomes available first. If that driver is still busy when a new delivery starts, then every other driver is also busy. Therefore, creating a new driver is necessary. This guarantees that no unnecessary drivers are created.

### Running Time:

- Sorting takes O(nlogn)
- Each delivery is added to or removed from the priority queue in O(logn)
- Total running time is O(nlogn)
