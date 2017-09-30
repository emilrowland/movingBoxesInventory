import os


def clear_console():
    for _ in range(10):
        print()


def print_list_of_moving_boxes(moving_boxes):
    print("ID\t|\tContent\t|\tPlace\t|\tAdded")
    for box in moving_boxes:
        print("{0[0]}\t|\t{0[1]}\t|\t{0[2]}\t|\t{0[3]}".format(box))


def print_moving_box(moving_box):
    print("ID\t|\tContent\t|\tPlace\t|\tAdded")
    print("{0[0]}\t|\t{0[1]}\t|\t{0[2]}\t|\t{0[3]}".format(moving_box))
