import basic


# calculator user interface
def main():
    while True:
        # main menu
        print("1. Basic functions")

        # dictionary for user selection
        selection = input("Select category. ")

        # evaluate selection
        match selection:
            case "1":
                basic.user_interface()
            case _:
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
            break


if __name__ == "__main__":
    main()
