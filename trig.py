from math import sin, cos, tan, asin, acos, atan, sinh, cosh, tanh, asinh,\
    acosh, atanh, pi


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
        print("\nConversion")
        print("1. Convert Degrees to Radians")
        print("2. Convert Radians to Degrees")

        print("\nNormal functions")
        print("3. Sine")
        print("4. Cosine")
        print("5. Tangent")
        print("6. Secant")
        print("7. Cosecant")
        print("8. Cotangent")

        print("\nHyperbolic Functions")
        print("9. Hyperbolic Sine")
        print("10. Hyperbolic Cosine")
        print("11. Hyperbolic Tangent")
        print("12. Hyperbolic Secant")
        print("13. Hyperbolic Cosecant")
        print("14. Hyperbolic Cotangent")

        print("\nInverse Functions")
        print("15. Inverse Sine")
        print("16. Inverse Cosine")
        print("17. Inverse Tangent")
        print("18. Inverse Hyperbolic Sine")
        print("19. Inverse Hyperbolic Cosine")
        print("20. Inverse Hyperbolic Tangent")

        # user selection
        selection = input("Select function. ")

        # take user input
        try:
            a = one_num_input()

            # evaluate selection
            if int(selection) in list(range(1, 3)):
                if selection == "1":  # degrees to radians
                    answer = deg_to_rad(a)

                    # print answer
                    print("Answer: {} radians".format(answer))

                elif selection == "2":  # radians to degrees
                    answer = rad_to_deg(a)

                    # print answer
                    print("Answer: {} degrees".format(answer))

            elif int(selection) in list(range(3, 9)):
                if selection == "3":  # sine
                    answer = sin(a)
                elif selection == "4":  # cosine
                    answer = cos(a)
                elif selection == "5":  # tangent
                    answer = tan(a)
                elif selection == "6":  # secant
                    answer = 1/cos(a)
                elif selection == "7":  # cosecant
                    answer = 1/sin(a)
                elif selection == "8":  # cotangent
                    answer = 1/tan(a)

                # print answer
                print("Answer: {}".format(answer))

            elif int(selection) in list(range(9, 15)):
                if selection == "9":  # hyp sine
                    answer = sinh(a)
                elif selection == "10":  # hyp cosine
                    answer = cosh(a)
                elif selection == "11":  # hyp tangent
                    answer = tanh(a)
                elif selection == "12":  # hyp secant
                    answer = 1/cosh(a)
                elif selection == "13":  # hyp cosecant
                    answer = 1/sinh(a)
                elif selection == "14":  # hyp cotangent
                    answer = 1/tanh(a)

                # print answer
                print("Answer: {}".format(answer))

            elif int(selection) in list(range(15, 21)):
                if selection == "15":  # inverse sine
                    radians = asin(a)
                elif selection == "16":  # inverse cosine
                    radians = acos(a)
                elif selection == "17":  # inverse tangent
                    radians = atan(a)
                elif selection == "18":  # inverse hyp sine
                    radians = asinh(a)
                elif selection == "19":  # inverse hyp cosine
                    radians = acosh(a)
                elif selection == "20":  # inverse hyp tangent
                    radians = atanh(a) 
                
                # convert to degrees
                degrees = radians / pi * 180

                # print in rad and deg
                print("Answer: {} ({} degrees)".format(radians, degrees)) 

            else:
                print("Invalid selection.\n")
                continue
            break

        except TypeError:
            continue

        except ValueError:
            print("No answer for input.\n")
