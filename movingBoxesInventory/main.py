from movingBox import MovingBox

def print_menu():
    """Print menu"""
    print("Moving boxes inventory")
    print("1.\tNew moving box")
    print("2.\tGet info on moving box")
    print("3.\tUpdate moving box status")
    print("4.\tUpdate moving box info")
    print("5.\tGet moving box list")
    print("6.\tGet next available moving box ID")
    print("7.\tExit application")


def main():
    """Main loop"""
    db = MovingBox()
    while True:
        print_menu()
        try:
            option = int(input("Select option: "))
        except ValueError:
            print("You need to enter an number as option!")
            print("Try again!")
            continue
        if option == 1:
            print("Creating new moving box")
        elif option == 7:
            break
        else:
            print("Can't find any option: {0}".format(option))
            print("Try again!")


main()