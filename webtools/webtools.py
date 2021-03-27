"""Main module."""
import math
import random
import colortools as color
# import clerk


def create_color_palette(color=None):
    return color


def create_base_css():
    print("You can either choose a primary color or let us randomize one for you.")
    primary = ""
    is_hex = False
    while not is_hex:
        primary = input("Enter hex code or press enter for random: ")
        if not primary.strip():
            # user hit enter, signifying they want a random color
            primary = color.generate_random_hex()
            print(f"The random color we selected for you is {primary}.")
            break
        # check user entry to make sure it meets hex code requirements
        is_hex = color.is_hex(primary)
        
    my_palette = color.color_palette_inator(primary)
    print(my_palette)


if __name__ == "__main__":
    create_base_css()
    c1 = create_color_palette("rgb")
    # color2 = create_color_palette()
    # print(c1)
    # print(color2)
    # palette = color.color_palette_inator("#336699")
    # print(palette)
