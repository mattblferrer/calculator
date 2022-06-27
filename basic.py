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
            print("Invalid input\n")


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
        return "Can't divide by 0"
    else:
        if is_integer and a % b == 0:
            return a // b  # will return an integer

        else:
            return a / b


# returns the remainder when a is divided by b
def remainder(a, b):
    if b == 0:
        return "Can't divide by 0"
    else:
        return a % b


# user interface
def user_interface():
    while True:
        # menu of functions
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Remainder")

        # user selection
        selection = input("Select function. ")

        # take user input
        try:
            a, b = two_num_input()

            # evaluate selection
            match selection:
                case "1":  # add
                    answer = add(a, b)
                case "2":  # subtract
                    answer = subtract(a, b)
                case "3":  # multiply
                    answer = multiply(a, b)
                case "4":  # divide
                    answer = divide(a, b)
                case "5":  # remainder
                    answer = remainder(a, b)
                case _:
                    print("Invalid selection.\n")
                    continue

            print("Answer: {} ({:e})".format(answer, answer))  # print in scientific notation
            break

        except TypeError:
            continue
