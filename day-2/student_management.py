def main():
    student_list = []
    is_running = True
    while is_running :
       is_running = menu(is_running, student_list)

def menu(is_running, student_list):
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("Press any no for Exit")
    opt = int(input("Enter the number : "))

    if opt == 1:
        add_student(student_list)
    elif opt == 2:
        view_student(student_list)
    elif opt == 3:
        search_student(student_list)
    elif opt == 4:
        delete_student(student_list)
    else:
        is_running = False
        print("Bye")
    return is_running

def add_student(student_list):
    student_data = {}
    student_name = input("Enter student name : ")
    student_age = int(input("Enter student age : "))
    student_marks = int(input("Enter student marks : "))
    student_data["name"] = student_name
    student_data["age"] = student_age
    student_data["marks"] = student_marks
    student_list.append(student_data)
    return student_list

def view_student(student_list):
    if len(student_list) == 0:
        print("\n\n\tdata not found\n\n")
    else:
        for student in student_list:
            print(f"\n\n\tStudent Name is {student['name']} Age is {student['age']} Marks is {student['marks']}\n\n")

def search_student(student_list):
    if len(student_list) == 0:
        print("No Data available")
    else:
        search_name = input("Enter student name for search : ")
        is_exist = False
        student_data_1 = {}
        for student_data in student_list:
            if student_data['name'] == search_name:
                is_exist = True
                student_data_1 = student_data
        if is_exist:
            print(f"\n\n\tStudent Name is {student_data_1['name']} Age is {student_data_1['age']} Marks is {student_data_1['marks']}\n\n")
        else:
            print('\n\tStudent Not Found\n')

def delete_student(student_list):
    delete_name = input("Enter student name")
    for data in student_list:
        if data['name'] == delete_name:
            print(student_list.remove(data))


if __name__ == "__main__":
    main()
