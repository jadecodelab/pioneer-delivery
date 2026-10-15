from scheduler import (
    read_deliveries, 
    select_max_deliveries, 
    assign_drivers, 
    minimum_rejected,)

def main():
    deliveries = read_deliveries("data.txt")

    # Task A
    selected_deliveries = select_max_deliveries(deliveries)

    print("Task A: Maximium deliveries for one driver")
    for delivery in selected_deliveries:
        print(f"{delivery['id']}: "
              f"{delivery['start']} - {delivery['finish']}")

    print(f"Total deliveries completed: {len(selected_deliveries)}")

    # Task B
    driver_schedules = assign_drivers(deliveries)

    print("\nTask B: Minimum number of drivers")
    for driver_number, schedule in driver_schedules.items():
        delivery_ids = [delivery["id"] for delivery in schedule]
        print(f"Driver {driver_number}: {' '.join(delivery_ids)}")

    print(f"Minimum drivers required: {len(driver_schedules)}")


    # Task C
    rejected_count = minimum_rejected(deliveries)

    print(f"\nTask C: Minimum deliveries rejected: {rejected_count}")


if __name__ == "__main__":
    main()
    
