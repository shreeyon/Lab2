data = []
while True:
    print("\nChoose an option:")
    print("1. Push (Stack)")
    print("2. Pop (Stack)")
    print("3. Enqueue (Queue)")
    print("4. Dequeue (Queue)")
    print("5. Display List")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        item = input("Enter item to push: ")
        data.append(item)
        print("Item pushed to stack.")
    elif choice == '2':
        if len(data) == 0:
            print("Stack is empty.")
        else:
            popped = data.pop()
            print("Popped from stack:", popped)
    elif choice == '3':
        item = input("Enter item to enqueue: ")
        data.append(item)
        print("Item added to queue.")
    elif choice == '4':
        if len(data) == 0:
            print("Queue is empty.")
        else:
            removed = data.pop(0)
            print("Dequeued from queue:", removed)
    elif choice == '5':
        print("Current list:", data)
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
