import json

def save_students(students):
    with open("students.json", "w") as studentx:
        json.dump(students, studentx)

def load_students():
    try:
        with open("students.json", "r") as studentx:
            return json.load(studentx)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
students = load_students()

def lines():
    print("=" *40)

def search_student(students):
    lines()
    print("    Search For Students")
    lines()
    if len(students) == 0:
        print("Sorry there is nothing to search")
        return
    
    keyword = input("Enter Student Name: ").strip()
    if keyword == "":
        print("Please enter a name next time.")
        return

    found = False

    for student in students:
        if keyword.lower() in student["name"].lower():
            print("Student Found")
            print(f"{student['name']} - {student['status']}")
            found = True

    if not found:
        print("Sorry, Student not found")

def add_student(students):
    lines()
    print("Welcome To Student Management System")
    lines()
    name = input("Student name: ").strip()
    age = int(input("Student age: "))

    new = {
        "name" : name,
        "age" : age,
        "course" : "ICT",
        "grades" : [],
        "status" : "Active"
    }

    students.append(new)
    print("Student Added Successfully")

def add_grades(students):
    lines()
    print("     Add Grades")
    lines()
    view_students(students)

    if len(students) == 0:
        return
    
    choose = int(input("Which student do you want to add grades for: "))
    if choose < 1 or choose > len(students):
        print("Invalid choice")
        return
    
    index = choose - 1
    
    if len(students[index]["grades"]) == 0:
        v = int(input("Add grades for Mathematics: "))
        w = int(input("Add grades for Database: "))
        x = int(input("Add grades for Programming: "))
        y = int(input("Add grades for Networking:  "))
        z = int(input("Add grades for Troubleshooting: "))

        grades = {
            "mathematics" : v,
            "database" : w,
            "programming" : x,
            "networking" : y,
            "troubleshooting" : z
        }

        students[index]["grades"].append(grades)
        print("Grades added successfully!")
    else:
        print("This student already has grades.")

def get_average(student):
    if len(student["grades"]) == 0:
        return 0
    grade = student["grades"][0]
    return sum(grade.values()) / len(grade)

def sort_students(students):
    if len(students) == 0:
        print("No students yet")
        return
    
    sorted_students = sorted(students, key=get_average, reverse=True)
    for i, student in enumerate(sorted_students, start=1):
        avg = get_average(student)
        print(f"{i}. {student['name']} - Average: {avg:.2f}")

def view_students(students):
    lines()
    print("     View Students")
    lines()
    if len(students) == 0:
        print("No students yet")
        return
    
    for i, student in enumerate(students, start=1):
        print(f"{i}. {student['name']}")
        print(f"        Age:    {student['age']}")
        print(f"        Status: {student['status']}")
        if len(student["grades"]) == 0:
            print("        Recorded Grades: Empty")
        else:
            for grade in student["grades"]:
                print(f"        Grades: {grade}")

def show_average(students):
    lines()
    print("     Students Averages")
    lines()
    if len(students) == 0:
        return

    for i, student in enumerate(students, start=1):
        avg = get_average(student)
        print(f"{i}. {student['name']}")
        
        if avg == 0:
            print("     No grades recorded")
        else:
            print(f"     Average: {avg:.2f}")
            if avg >= 50:
                print("     PASSED!")
            else:
                print("     FAILED!")

def top_student(students):
    lines()
    print("     Top Student")
    lines()

    if len(students) == 0:
        return
    
    top = max(students, key=get_average)
    avg = get_average(top)

    if avg == 0:
        print("No grades recorded for any student")
        return
    
    print(f"Top student: {top['name']}")
    print(f"Average: {avg:.2f}")

def delete_student(students):
    lines()
    print("     Delete Student")
    view_students(students)

    if len(students) == 0:
        return
    
    delete = int(input("Which student do you wanna delete: "))
    if delete < 1 or delete > len(students):
        print("Invalid Input")
        return
    
    index = delete - 1
    students.pop(index)
    print("Student removed successfully")

def summary(students):
    lines()
    print("     STUDENT SUMMARY")
    lines()

    if len(students) == 0:
        print("No Students available")
        return
    
    total = len(students)
    passed = 0
    failed = 0

    for student in students:
        avg = get_average(student)
        if avg == 0:
            continue 
        if avg >= 50:
            passed += 1
        else:
            failed += 1

    print(f"Total Students: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

def menu():
    while True:
        lines()
        print("       MAIN MENU")
        lines()
        try:
            menu = [
                "0. Search Student",
                "1. Add Student",
                "2. View Students",
                "3. Delete Student",
                "4. Add Grades",
                "5. Show Averages",
                "6. Sort Students",
                "7. Top Student",
                "8. Class Summary",
                "9. Exit"
            ]

            for item in menu:
                print(item)

            lines()
            choose = int(input("Choose Option: "))

            if choose == 0:
                search_student(students)
            elif choose == 1:
                add_student(students)
                save_students(students)
            elif choose == 2:
                view_students(students)
            elif choose == 3:
                delete_student(students)
                save_students(students)
            elif choose == 4:
                add_grades(students)
                save_students(students)
            elif choose == 5:
                show_average(students)
            elif choose == 6:
                sort_students(students)
            elif choose == 7:
                top_student(students)
            elif choose == 8:
                summary(students)
            elif choose == 9:
                print("Thank you for using the application")
                break

        except ValueError:
            print("Invalid Option")

menu()