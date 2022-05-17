print("This is a Simple CLI Calculator. Ensure you pass in a number")
try:

    num1 = int (input("Enter the first Number: "))
    num2 = int (input("Enter the second Number: "))

    print("Operation available are 'add','minus','divide','multiply' and 'modulus'.")
    operation = input("Which operation do you want to perform: ")
    available_operand = ['add','minus','divide','multiply', 'modulus']
    if operation in available_operand:
        if operation == "add":
            operator = "addition"
            value = num1 + num2
        elif operation == "minus":
            operator = "subtraction"
            value = num1 - num2
        elif operation == "divide":
            operator = "division"
            value = num1 / num2
        elif operation == "multiply":
            operator = "multiplication"
            value = num1 * num2
        elif operation == "modulus":
            operator = "modulus"
            value = num1 % num2
        print(f"The {operator} of {num1} and {num2} is", value)

    else:
        print("INVALID OPERATION PASSED IN CLI Calculator")

except ValueError:
    print("You have just passed in invalid number!!! \n ")