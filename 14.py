products = {}

while True:
    print("\n===== Product Menu =====")
    print("1. Add new product")
    print("2. Update product price")
    print("3. Show all products")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        products[name] = price
        print("Product added")

    elif choice == "2":
        name = input("Enter product name to update price: ")
        if name in products:
            price = float(input("Enter new price: "))
            products[name] = price
            print("Price updated")
        else:
            print("Product not found")

    elif choice == "3":
        if products:
            print("\nProduct List:")
            for name, price in products.items():
                print(f"{name}: Rs. {price:.2f}")
        else:
            print("No products to show.")

    elif choice == "4":
        break

    else:
        print("Invalid choice. Please enter 1 to 4.")
