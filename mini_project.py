students = {}

while True:
    print("\n===== Student Report Card Management System =====")
    print("1. Add new student record")
    print("2. View all student reports")
    print("3. Display topper(s) of the class")
    print("4. Search student by roll number")
    print("5. Display students who failed in one or more subjects")
    print("6. Update marks of a student")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        roll_no = input("Enter roll number: ")
        if roll_no in students:
            print("Student with this roll number already exists.")
            continue
        name = input("Enter student name: ")
        marks = []
        num_subjects = int(input("Enter number of subjects: "))
        for i in range(num_subjects):
            mark = int(input(f"Enter marks for subject {i+1}: "))
            marks.append(mark)
        students[roll_no] = {"name": name, "marks": marks}
        print("Student record added.")

    elif choice == "2":
        if not students:
            print("No student records found.")
        else:
            print("\nAll Student Reports:")
            for roll_no in students:
                print(f"Roll No: {roll_no}, Name: {students[roll_no]['name']}")
                print("Marks:")
                marks = students[roll_no]['marks']
                for m in marks:
                    print(m)
                average = sum(marks) / len(marks)
                print(f"Average: {average:.2f}")

    elif choice == "3":
        if not students:
            print("No student records found.")
            continue
        highest_avg = -1
        toppers = []
        for roll_no in students:
            marks = students[roll_no]["marks"]
            avg = sum(marks) / len(marks)
            if avg > highest_avg:
                highest_avg = avg
                toppers = [students[roll_no]["name"]]
            elif avg == highest_avg:
                toppers.append(students[roll_no]["name"])
        print(f"Topper(s) with average {highest_avg:.2f}:")
        for name in toppers:
            print(name)

    elif choice == "4":
        roll_no = input("Enter roll number to search: ")
        if roll_no in students:
            print(f"Roll No: {roll_no}, Name: {students[roll_no]['name']}")
            print("Marks:")
            marks = students[roll_no]['marks']
            for m in marks:
                print(m)
            average = sum(marks) / len(marks)
            print(f"Average: {average:.2f}")
        else:
            print("Student not found.")

    elif choice == "5":
        failed_students = []
        for roll_no in students:
            marks = students[roll_no]["marks"]
            if any(mark < 40 for mark in marks):
                failed_students.append((roll_no, students[roll_no]["name"]))
        if failed_students:
            print("Students failed in one or more subjects:")
            for roll_no, name in failed_students:
                print(f"Roll No: {roll_no}, Name: {name}")
        else:
            print("No students have failed.")

    elif choice == "6":
        roll_no = input("Enter roll number to update marks: ")
        if roll_no in students:
            num_subjects = int(input("Enter number of subjects: "))
            new_marks = []
            for i in range(num_subjects):
                mark = int(input(f"Enter new marks for subject {i+1}: "))
                new_marks.append(mark)
            students[roll_no]["marks"] = new_marks
            print("Marks updated.")
        else:
            print("Student not found.")

    elif choice == "7":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter 1 to 7.")
