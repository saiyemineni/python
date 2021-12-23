from Art import logo
import os

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide
}


def Calculator():
    print(logo)
    num1 = float(input("what's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("what's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        response = input(f"Type 'y' to conitinue calculating with {answer}, or 'n' to start a new calcualtion or 'exit' to exit from calculator: ").lower()
        if response == 'y':
            num1 = answer
        elif response == 'exit':
            should_continue = False
            print(f"Your final answer is {answer}")
            print("Thank you.")
        else:
            should_continue = False
            Calculator()


Calculator()


