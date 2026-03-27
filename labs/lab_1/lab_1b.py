"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""

import numbers
def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide' again.")
        

def check_if_number(value):
    try:
        float(value)
        return True
    except Exception as e:
        return False
    



def main():
    
    print(f"===== Simple Calculator =====")


# Ask the user for sample input    
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    my_list= ["add","subtract","multiply","divide"]
        

    InputCorrect = check_if_number(num1) and check_if_number(num2) and operation in my_list
    if(not InputCorrect):
        print("The numbers/operations entered are incorrect. Try again!!")

   
    while not InputCorrect:
        # Ask the user for sample input    
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

        InputCorrect = check_if_number(num1) and check_if_number(num2) and operation in my_list

        if(not InputCorrect):
            print("The numbers/operations entered are incorrect. Try again!!")

# Perform the calculation and display the result
    result = simple_calculator(operation, float(num1), float(num2))
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")


    


if __name__ == "__main__":
    main()
