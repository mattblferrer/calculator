from math import log


# two number input
def two_num_input():
    a = input("Enter first number: ")
    b = input("Enter second number: ")

    # int or float input
    try:
        return int(a), int(b)
    except ValueError:
        try:
            return float(a), float(b)
        except ValueError:  # invalid data types
            print("Invalid input.\n")


# adds two numbers a and b
def add(a, b):
    return a + b


# subtracts two numbers a and b
def subtract(a, b):
    return a - b


# multiplies two numbers a and b
def multiply(a, b):
    return a * b


# divides two numbers a and b
def divide(a, b):
    is_integer = isinstance(a, int) and isinstance(b, int)

    if b == 0:
        return "Can't divide by 0."
    else:
        if is_integer and a % b == 0:
            return a // b  # will return an integer

        else:
            return a / b


# returns the remainder when a is divided by b
def remainder(a, b):
    if b == 0:
        return "Can't divide by 0."
    else:
        return a % b


# returns a^b
def power(a, b):
    return a ** b


# returns logb(a)
def logarithm(a, b):
    try:
        return log(a, b)
    except ZeroDivisionError:
        print("Can't divide by 0.\n")


# user interface
def user_interface():
    while True:
        # menu of functions
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Remainder")
        print("6. Exponent")
        print("7. Logarithm")

        # user selection
        selection = input("Select function. ")

        # take user input
        try:
            a, b = two_num_input()

            # evaluate selection
            if selection == "1":  # add
                answer = add(a, b)
            elif selection == "2":  # subtract
                answer = subtract(a, b)
            elif selection == "3":  # multiply
                answer = multiply(a, b)
            elif selection == "4":  # divide
                answer = divide(a, b)
            elif selection == "5":  # remainder
                answer = remainder(a, b)
            elif selection == "6":  # power
                answer = power(a, b)    
            elif selection == "7":  # logarithm
                answer = logarithm(a, b)
            else:
                print("Invalid selection.\n")
                continue

            # print in scientific notation
            print("Answer: {} ({:e})".format(answer, answer))  
            break

        except TypeError:
            continue
