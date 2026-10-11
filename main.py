from scheduler import read_deliveries, assign_drivers, minimum_rejected

def main():
    deliveries = read_deliveries("data.txt")
    driver_schedules = assign_drivers(deliveries)

    for driver_number, schedule in driver_schedules.items():
        delivery_ids = [delivery["id"] for delivery in schedule]
        print(f"Driver {driver_number}: {' '.join(delivery_ids)}")

    print(f"\nMinimum drivers required: {len(driver_schedules)}")

    rejected_count = minimum_rejected(deliveries)

    print(f"\nMinimum deliveries rejected: {rejected_count}")


if __name__ == "__main__":
    main()
    
