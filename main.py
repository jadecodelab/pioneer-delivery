from scheduler import read_deliveries, select_max_deliveries

def main():
    deliveries = read_deliveries("data.txt")
    selected = select_max_deliveries(deliveries)

    for delivery in selected:
        print(delivery["id"], delivery["start"], delivery["finish"])


if __name__ == "__main__":
    main()
    
