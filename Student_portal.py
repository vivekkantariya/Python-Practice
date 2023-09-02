import turtle as t

t.Screen()
t.hideturtle()
t.setup(800, 600)
t.bgcolor("powderblue")
t.title("Menu of Students")
t.penup()
t.goto(-320, 110)
t.write("-:The Menu Contains The Following List:-", font=("Calibri", 20, "bold"))
t.goto(-170, 260)
t.write("Student Details in Menu", font=("Calibri", 26, "bold"))
t.hideturtle()
t.goto(-340, 40)
t.write("i) To Store student Details :-  ", font=("Calibri", 20, "bold"))
t.goto(-340, 0)
t.write("ii) Details of a Student With his Roll No  :-  ", font=("Calibri", 20, "bold"))
t.goto(-340, -40)
t.write("iii) To Print the Percentage of all the Students :-  ", font=("Calibri", 20, "bold"))
t.goto(-340, -80)
t.write("iv) Top 10 Students from the above :-", font=("Calibri", 20, "bold"))
t.goto(-340, -120)
t.write("v) Exit 🎆 :-", font=("Calibri", 20, "bold"))
t.goto(-340, -200)
t.write("For Detailed Information of Students See in the Terminal ", font=("Calibri", 22, "bold"))
t.goto(220, -260)
t.write("Created by Vivek Kantariya")
t.goto(220, -280)
t.write("216200316051")

Main = {}

print()
print("1: Store student Details")
print("2: Details of a Student with his Roll no :- ")
print("3: Print the Percentage of all the Students ")
print("4: Top 10 Students from the Above ")
print("5: Exit 🎆")
print()

while True:
    print()

    choice = int(input("Enter your choice :- "))

    if choice == 1:
        number = int(input("Number Of Students:- "))
        student_number = 1

        for i in range(1, 1 + number):
            print("\n Student Number ", student_number, ":")
            name = (input("Enter Student Name:- "))
            roll_no = (input("Enter Student's Roll no:- "))
            student_age = (input("Enter age of a Student :-"))
            gender = (input("Enter Student's Gender :- "))
            percentage = (input("Enter Student's Percentage:- "))

            student_number += 1

            Main[roll_no] = [{"Name": name, "Roll NO": roll_no, "Age_of_Student": student_age, "Gender": gender,"Percentage": percentage, }]

            l = [name, roll_no, student_age, gender, percentage]

            file = open("Portal.txt", "a")
            file.write(str(l))
            file.write("\n")
            if file:
                print("\n Data Stored Successfully")
            file.close()


    elif choice == 2:
        file = open("Portal.txt", "r")
        n = input("Details of a Student Enter His/Her Roll No:- ")
        num = Main[n][0]
        for i in num.items():
            print(i)
        file.readlines()
        file.close()

    elif choice == 3:
        file = open("Portal.txt", "r")
        print("Print the Percentage of all the students:-")

        for i in Main.keys():
            print(Main[i][0]["Name"], '=', Main[i][0]["Percentage"])

        file.readlines()
        file.close()

    elif choice == 4:
        print("Top 10 Students from the Above is: ")

        file = open('Portal.txt', 'r')
        data = file.readlines()
        file.close()

        top_10 = sorted(data, key=lambda x: int(x[-4:-3:]), reverse=True)

        for i in range(10):
            print(top_10[i])

    elif choice == 5:
        print("Rate Us on Micro Project Marks: ☺️")

    else:
        print("PLease Enter Valid Choice Number")
