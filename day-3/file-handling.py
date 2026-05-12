import json
import traceback
def add_student():
    try:
        student_id = int(input("Enter student id : "))
        student_name = input("Enter student name : ")
        student_age = int(input("Enter student age : "))
        student_marks = int(input("Enter student marks : "))
        student_exist = False
        student_object = {"id":student_id, "name":student_name, "age": student_age, "marks":student_marks}
        if student_marks < 0 and student_marks > 100:
            print("Please give valid marks")
        else:
            with open("students.json", "r") as file:
                lines  = json.load(file)
                for line in lines:
                    if line.get("id") == student_id:
                        student_exist = True
                        print("Student exist")
                if not student_exist:
                    lines.append(student_object)
                    with open("students.json", "w") as file:
                        json.dump(lines, file)
    except ValueError as error:
        print(error)

def view_student_data():
    try:
        with open("students.json", "r") as file:
            lines = json.load(file)
            for line in lines:
                print(line)
    except Exception as error:
        print("File not found")

def update_marks():
    try:
        student_id = int(input("Enter Student id : "))
        student_marks = int(input("Enter new marks : "))
        if 0 <= student_marks <= 100:
            student_data = []
            with open("students.json", "r") as file:
                    lines  = json.load(file)
                    for line in lines:
                        if line.get("id") == student_id:
                            line["marks"] = student_marks
                            student_data.append(line)
                        else:
                            student_data.append(line)
            with open("students.json", "w") as file:
                print("file write")
                json.dump(student_data, file)
        else:
            print("Please enter valid marks")
    except ValueError as error:
        print(f"Invalid input: {error}")

def menu(is_running):
    try:
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student marks")
        print("Press any no for Exit")
        opt = int(input("Enter the number : "))
        if opt == 1:
            add_student()
        elif opt == 2:
            view_student_data()
        elif opt == 3:
            update_marks()
        else:
            is_running = False
    except Exception as error:
        traceback.print_exc()
    return is_running


def main():
    is_running = True
    while is_running :
       is_running = menu(is_running)

if __name__ == "__main__":
    main()