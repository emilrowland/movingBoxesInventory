from movingBox import MovingBox
from addMovingBox import AddMovingBox
from getMovingBox import GetMovingBox
import utility


def print_menu():
    """Print menu"""
    print("Moving boxes inventory")
    print("1.\tNew moving box")
    print("2.\tGet info on moving box")
    print("3.\tUpdate moving box status")
    print("4.\tUpdate moving box info")
    print("5.\tGet moving box list")
    print("6.\tExit application")


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
            new_moving_box = AddMovingBox(db)
            new_moving_box.add_moving_box()
        elif option == 2:
            moving_box = GetMovingBox(db)
            moving_box.interface()
        elif option == 5:
            utility.print_list_of_moving_boxes(db.get_all_moving_boxes())
        elif option == 6:
            break
        else:
            print("Can't find any option: {0}".format(option))
            print("Try again!")


main()
