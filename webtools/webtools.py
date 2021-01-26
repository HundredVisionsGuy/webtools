"""Main module."""
import math
import random
hex_map = {"0": 0,
           "1": 1,
           "2": 2,
           "3": 3,
           "4": 4,
           "5": 5,
           "6": 6,
           "7": 7,
           "8": 8,
           "9": 9,
           "a": 10,
           "b": 11,
           "c": 12,
           "d": 13,
           "e": 14,
           "f": 15}


def rgb_to_hex(*args):
    # are there three separate values or 1 string
    if len(args) == 3:
        r, g, b = args
    else:
        try:
            rgb = args[0]
            r, g, b = extract_rgb_from_string(rgb)
        except:
            # throw an exception
            return "err"
    # Convert r, g, b to hex
    r = hex(int(r))[2:]
    g = hex(int(g))[2:]
    b = hex(int(b))[2:]
    # prepend 0 if necessary
    if len(r) == 1:
        r = "0" + r
    if len(g) == 1:
        g = "0" + g
    if len(b) == 1:
        b = "0" + b
    return "#" + r + g + b


def hex_to_rgb(hex):
    """ receives hex (str) -> returns rgb as tuple """
    if "#" in hex[0]:
        hex = hex[1:]
    r = hex[:2]
    g = hex[2:4]
    b = hex[4:]

    r = hex_to_decimal(r)
    g = hex_to_decimal(g)
    b = hex_to_decimal(b)

    return (r, g, b)


def rgb_as_string(rgb):
    """ receive rgb as tuple -> returns formatted string """
    r, g, b = rgb
    return f"rgb({r},{g},{b})"


def hex_to_decimal(c):
    ones = hex_map[c[1]]
    sixteens = hex_map[c[0]] * 16
    return sixteens + ones


def get_background_from_hsl(hsl):
    h, s, l = hsl
    l = 97
    return (h, s, l)


def get_text_from_hsl(hsl):
    h, s, l = hsl
    l = 10
    return (h, s, l)


def rgb_to_hsl(rgb):
    """ receives rgb as tuple -> returns hsl as tuuple """
    r, g, b = rgb
    # Make r, g, and b fractions of 1
    r /= 255
    g /= 255
    b /= 255

    # Find greatest and smallest channel values
    c_min = min(r, g, b)
    c_max = max(r, g, b)
    delta = c_max - c_min

    h = 0
    s = 0
    l = 0

    # is red max?
    if delta == 0:
        h = 0
    elif c_max == r:
        h = ((g - b) / delta) % 6
    elif c_max == g:
        h = (b - r) / delta + 2
    else:
        h = (r - g) / delta + 4
    h = round(h * 60)

    # make sure h is a positive integer
    h %= 360

    # calculate lightness
    l = (c_max + c_min) / 2

    # Calculate saturation
    if delta == 0:
        s = 0
    else:
        s = delta / (1 - abs(2 * l - 1))

    # convert s & l to values out of 100%
    # multiply them by 100 and round to the nearest tenth
    s = round(s * 100)
    l = round(l * 100)

    return (h, s, l)


def hsl_as_string(hsl):
    """ Return hsl as a formatted string """
    h, s, l = hsl
    return f"hsl({h},{s}%,{l}%)"


def extract_rgb_from_string(rgb):
    output = []
    if "," in rgb:
        sep = ","
    else:
        sep = " "
    rgb = rgb.split(sep)
    for i in rgb:
        try:
            output.append(i.split("(")[1].strip())
            continue
        except:
            try:
                output.append(i.split(")")[0].strip())
            except:
                output.append(i.strip())
                continue

    return output[0], output[1], output[2]


def random_rgb():
    """ generates and returns random rgb """
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)
    return (r, g, b)


def color_palette_inator():
    """ generates a complete color palette of HSL (dict) """
    palette = {
        "primary": (),
        "background": (),
        "text": (),
        "alerts": {
            "success": (),
            "warning": (),
            "failure": (),
        },
        "links": {
            "link": (),
            "visited": (),
            "hover": (),
        },
        "triad": {
            "color1": {
                "color": (),
                "shades": {
                    "dark": (),
                    "med-dark": (),
                    "med": (),
                    "med-light": (),
                    "light": (),
                    "lightest": (),
                }
            },
            "color2": {
                "color": (),
                "shades": {
                    "dark": (),
                    "med-dark": (),
                    "med": (),
                    "med-light": (),
                    "light": (),
                    "lightest": (),
                }
            }
        },
        "tertiary": {
            "color1": {
                "color": (),
                "shades": {
                    "dark": (),
                    "med-dark": (),
                    "med": (),
                    "med-light": (),
                    "light": (),
                    "lightest": (),
                }
            },
            "color2": {
                "color": (),
                "shades": {
                    "dark": (),
                    "med-dark": (),
                    "med": (),
                    "med-light": (),
                    "light": (),
                    "lightest": (),
                }
            },
            "color3": {
                "color": (),
                "shades": {
                    "dark": (),
                    "med-dark": (),
                    "med": (),
                    "med-light": (),
                    "light": (),
                    "lightest": (),
                }
            }
        },
    }
    primary = rgb_to_hsl(random_rgb())
    palette["primary"] = primary
    palette["background"] = get_background_from_hsl(primary)
    palette["text"] = get_text_from_hsl(primary)
    return palette


if __name__ == "__main__":
    print(rgb_to_hex(10, 10, 10))
    print(rgb_to_hex("rgb(10 0 0)"))
    rgb = hex_to_rgb("#336699")
    print(rgb_as_string(rgb))
    rgb = hex_to_rgb("#336699")
    print(f"#336699 as rgb is rgb{rgb}")
    hsl = rgb_to_hsl(rgb)
    print(hsl_as_string(hsl))
    random.seed(1)
    for i in range(3):
        print(random_rgb())
    palette = color_palette_inator()
    print(palette)
    rgb = random_rgb()
    hsl = rgb_to_hsl(rgb)
    print(f"hsl = {hsl}")
    bg = get_background_from_hsl(hsl)
    print(f"background color is {bg}")
    text = get_text_from_hsl(hsl)
    print(f"text color is {text}")
