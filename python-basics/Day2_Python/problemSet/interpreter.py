# In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

# x is an integer
# y is +, -, *, or /
# z is an integer
# For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

import operator

# First step is to get user input for a mathematical formula but the assumed input would be a string that needs to be converted into 2 integers, and an operator.
def mathInt():
    formula = input("Please enter a basic algebra equation: ")
    # Need to separate the string into 3 strings using white space.
    equation = formula.split(" ")
    # Create map for operators
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "**": operator.pow,
        "%": operator.mod
    }
    #establish x, y, z values and convert to x and z to integers
    x = int(equation[0])
    y = equation[1]
    z = int(equation[2])

    # if y is in ops return the value of the equation x y z
    if y in ops:
        result = ops[y] (x, z)
        print(f"{x} {y} {z} = {result}")
    # else return that there is an unknown operator
    else:
        print(f"Unknown operator: {y}")

mathInt()