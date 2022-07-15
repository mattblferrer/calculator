from math import sin, cos, tan, asin, acos, atan, pi


# one number input
def one_num_input():
    a = input("Enter number: ")

    # int or float input
    try:
        return int(a)
    except ValueError:
        try:
            return float(a)
        except ValueError:  # invalid data types
            print("Invalid input.\n")

        
# converts from degrees to radians
def deg_to_rad(a):
    return a / 180 * pi


# converts from radians to degrees
def rad_to_deg(a):
    return a / pi * 180


# user interface
def user_interface():
    while True:
        # menu of functions
        print("1. Sine")
        print("2. Cosine")
        print("3. Tangent")
        print("4. Inverse Sine")
        print("5. Inverse Cosine")
        print("6. Inverse Tangent")
        print("7. Convert Degrees to Radians")
        print("8. Convert Radians to Degrees")

        # user selection
        selection = input("Select function. ")

        # take user input
        try:
            a = one_num_input()

            # evaluate selection
            if int(selection) in list(range(1, 7)):
                if selection == "1":  # sine
                    radians = sin(a)
                elif selection == "2":  # cosine
                    radians = cos(a)
                elif selection == "3":  # tangent
                    radians = tan(a)
                elif selection == "4":  # inverse sine
                    radians = asin(a)
                elif selection == "5":  # inverse cosine
                    radians = acos(a)
                elif selection == "6":  # inverse tangent
                    radians = atan(a)   
                
                # convert to degrees
                degrees = radians / pi * 180

                # print in rad and deg
                print("Answer: {} ({} degrees)".format(radians, degrees)) 

            elif int(selection) in list(range(7, 9)):
                if selection == "7":  # degrees to radians
                    answer = deg_to_rad(a)

                    # print answer
                    print("Answer: {} radians".format(answer))

                elif selection == "8":  # radians to degrees
                    answer = rad_to_deg(a)

                    # print answer
                    print("Answer: {} degrees".format(answer))

            else:
                print("Invalid selection.\n")
                continue
            break

        except TypeError:
            continue

        except ValueError:
            print("No answer for input.\n")
