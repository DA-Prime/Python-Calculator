#Explain how to use the calculator to the user
#Ask for 2 floating point inputs(Ask for 1st float variable, then the math function, and last but not least the second input)

program = "Yes"
while program == "yes" or program == "Yes" or program == "Y" or program == "y":
    print("Welcome to the Thonny Calculator, here is how to use the calculator, when the program demands '1st Number please: ' you type in a number")
    print("of your choice (can be whole, decimal, or negative) and click enter. Next it will ask 'Python Math Operator please' and you choose")
    print("which function should be used and below is the list of functions and what each one does.")
    print("\n- '+' is to add the two numbers together")
    print("- '-' is to subtract the 2nd number from the 1st number")
    print("- '*' is to multiply the two numbers together")
    print("- '/' is to divide the 1st number by the 2nd number (just don't divide the first number by zero)")
    print("- '//' is to divide the 1st number by the 2nd number for a non-decimal result (again, don't divide the numerator by zero)")
    print("- '%' is to find the remainder of the function if the 1st number was inserted to be divided by the 2nd number")
    print("- '**' is to have the 1st number be multiplied by the number that is in the second number")
    print("\nWhen the program asks'2nd Number please: ' type in and enter any number of your choice (whole, decimal or a negative number)")
    print("to have the function play out a result based on what you typed in")

    num1 = float(input("\n1st Number please: "))
    function = str(input("\nPython Math Operator please: "))
    num2 = float(input("\n2nd Number please: "))

    if function == "+":
        print("\n", num1 + num2)

    elif function == "-":
        print("\n", num1 - num2)

    elif function == "*":
        print("\n", num1 * num2)

    elif function == "/":
        print("\n", num1 / num2)

    elif function == "//":
        print("\n", int(num1 // num2))

    elif function == "%":
        print("\n", num1 % num2)

    elif function == "**":
        print("\n", num1 ** num2)

    pro = input("\nDo you want to run the calculator again (Y or N?): ")
    if pro == "yes" or pro == "Yes" or pro == "Y" or pro == "y":
        continue
    else:
        break