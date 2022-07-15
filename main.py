import basic
import trig


# calculator user interface
def main():
    while True:
        # main menu
        print("1. Basic functions")
        print("2. Trigonometric Functions")

        # dictionary for user selection
        selection = input("Select category. ")

        # evaluate selection
        if selection == "1":
            basic.user_interface()
        elif selection == "2":
            trig.user_interface()
        else:
            print("Invalid selection.\n")

        # restart
        while True:
            restart = input("Do you want to restart? (Y/N) ").upper()
            if restart in ["Y", "N"]:
                break
            print("Invalid input.\n")

        if restart == "Y":
            print("")
            continue
        else:
            print("Thank you for using the calculator!\n")
            break


if __name__ == "__main__":
    main()
