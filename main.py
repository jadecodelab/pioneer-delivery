from scheduler import read_deliveries

def main():
    deliveries = read_deliveries("data.txt")

    for delivery in deliveries:
        print(delivery["id"], delivery["start"], delivery["finish"])


if __name__ == "__main__":
    main()
    
