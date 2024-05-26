print ("******************** CALCULATOR ********************")

num1 = float(input("enter the first number here"))
num2 = float(input("Enter the second number here:"))

while True: #using loop so program will continue until user enter correct numbers
    print("Enter 1 for 'Addition'\n Enter 2 for 'Subtraction'\n Enter 3 for 'Multiplication'\n Enter 4 for 'Division'")
    enter_num = int(input("chose a number from 1 to 4"))

    if enter_num == 1:
        print("Addition of your 1st and 2nd number is :", num1 + num2)
        break
    elif enter_num == 2:
        print("Subtraction of your 1st and 2nd number is :", num1 - num2)
        break
    elif enter_num == 3:
        print("Multiplication of your 1st and 2nd number is :", num1 * num2)
        break
    elif enter_num == 4:
        print("Division of your 1st and 2nd number is :", num1 / num2)
        break
    else:
        print("invalid input")