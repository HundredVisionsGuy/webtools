"""Main module."""
import math
import random
import colortools as color


def create_color_palette(color=None):
    return color


def create_base_css():
    print("You can either choose a primary color or let us randomize one for you.")
    primary = ""
    is_hex = False
    while not is_hex:
        primary = input("Enter hex code or press enter for random: ")
        
        # if the user hits enter, without 
        if not primary.strip():
            primary = color.generate_random_hex()
            print(f"The random color we selected for you is {primary}.")
            break

        # check user entry to make sure it meets hex code requirements
        is_hex = color.is_hex(primary)
        
    my_palette = color.color_palette_inator(primary)
    return my_palette


if __name__ == "__main__":
    p1 = create_base_css()
    # c1 = color.color_palette_inator("rgb")
    hsl = p1["background"]
    r,g,b = color.hsl_to_rgb(hsl)
    bg = color.rgb_to_hex(r,g,b)
    hsl = p1["text"]
    r,g,b = color.hsl_to_rgb(hsl)
    text = color.rgb_to_hex(r,g,b)
    print("Background: " + bg)
    print("Text: " + text)
