# Pioneer Delivery Algorithm Portfolio Part II

## Programming Language

Python

## How to Run the Algorithms

Open a terminal in the project folder and run:

```text
cd part2
python closest_pair.py
```

# Task A: Closest Delivery Locations

## Goal

Task A finds the two delivery locations that are closest to each other.

Each location contains: (location_id, x_coordinate, y_coordinate)

The program returns:

- The IDs of the closest pair
- Their squared distance

## Algorithm

The program uses a divide-and-conquer algorithm.

1. Sort all points by their x-coordinate.
2. Divide the points into a left half and a right half.
3. Recursively find the closest pair in the left half.
4. Recursively find the closest pair in the right half.
5. Keep the smaller distance from the two halves.
6. Create a vertical strip around the dividing line.
7. Sort the strip points by their y-coordinate.
8. Check each point against only a small number of nearby points in the strip.
9. Return the closest pair found.

## Running Time

O(nlogn)
