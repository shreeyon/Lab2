students = {
    "Shriyon": [85, 90, 78],
    "Binupa": [98, 97, 99],
    "Ram": [95, 85, 87]
}

while True:
    print("\n===== Student Menu =====")
    print("1. Display average marks of each student")
    print("2. Find the topper")
    print("3. Update marks of a student")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        for name, marks in students.items():
            average = sum(marks) / len(marks)
            print(f"{name}: Average = {round(average, 2)}")

    elif choice == "2":
        topper = ""
        highest_avg = 0
        for name, marks in students.items():
            avg = sum(marks) / len(marks)
            if avg > highest_avg:
                highest_avg = avg
                topper = name
        print(f"Topper: {topper} with average {round(highest_avg, 2)}")

    elif choice == "3":
        name_to_update = input("Enter student name to update marks: ")
        if name_to_update in students:
            num_marks = int(input("Enter number of marks: "))
            new_marks = []
            for _ in range(num_marks):
                mark = int(input())
                new_marks.append(mark)
            students[name_to_update] = new_marks
            print("Updated")
        else:
            print("No student found")

    elif choice == "4":
        break

    else:
        print("Invalid choice. Please enter 1 to 4.")
