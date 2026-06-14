names = []
m = []
c = []
p = []
r = []

def Add_Students():
    name = input("Enter Students Name : ")
    ma = int(input("Enter Mathematics Score = "))
    cm = int(input("Enter Chemistry Score = "))
    ph = int(input("Enter Physics Score = "))
    roll_no = int(input("Enter Student Roll No. : "))

    names.append(name)
    m.append(ma)
    c.append(cm)
    p.append(ph)
    r.append(roll_no)

    print(f"{name} added successfully!")

def Grade():
    name = input("Enter Student Name : ")

    if name in names:
        index = names.index(name)

        Total_Marks = m[index] + c[index] + p[index]
        percentage = (Total_Marks / 300) * 100

        print(f"Total Marks = {Total_Marks}")
        print(f"Percentage = {percentage:.2f}%")

        if percentage >= 95:
            print("Grade : A")

        elif percentage >= 80:
            print("Grade : B")

        elif percentage >= 65:
            print("Grade : C")

        elif percentage >= 35:
            print("Grade : D")

        else:
            print("Fail")

    else:
        print("Student not found!")

def Search_student():
    name = input("Enter student name to search : ")

    if name in names:
        index = names.index(name)

        print(f"Student : {names[index]}")
        print(f"Roll No : {r[index]}")
        print(f"Math = {m[index]}")
        print(f"Physics = {p[index]}")
        print(f"Chemistry = {c[index]}")

    else:
        print("Student not found!!")

def Display_Result_Card():
    print("\n----Student Records----")

    for i in range(len(names)):
        print(f"\nName : {names[i]}")
        print(f"Roll No. = {r[i]}")
        print(f"Math = {m[i]}")
        print(f"Physics = {p[i]}")
        print(f"Chemistry = {c[i]}")

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students_Record_Card")
    print("3. Search Student")
    print("4. Grade")
    print("5. Exit")

    choice = int(input("Enter ur choice : "))

    if choice == 1:
        Add_Students()

    elif choice == 2:
        Display_Result_Card()

    elif choice == 3:
        Search_student()

    elif choice == 4:
        Grade()

    elif choice == 5:
        print("Exit")
        break

    else:
        print("Invalid Choice!")