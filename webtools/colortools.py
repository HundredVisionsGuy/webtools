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


def generate_random_hex():
    color = "#"
    for i in range(6):
        color += random.choice(list(hex_map.keys()))
    return color

def hex_to_rgb(hex_code):
    """ receives hex (str) -> returns rgb as tuple """
    hex_code = hex_code.lower()
    if "#" in hex_code[0]:
        hex_code = hex_code[1:]
    r = hex_code[:2]
    g = hex_code[2:4]
    b = hex_code[4:]

    r = hex_to_decimal(r)
    g = hex_to_decimal(g)
    b = hex_to_decimal(b)

    return (r, g, b)


def rgb_as_string(rgb):
    """ receive rgb as tuple -> returns formatted string """
    r, g, b = rgb
    return f"rgb({r},{g},{b})"


def hex_to_decimal(c):
    # make sure to convert to lower case
    # so FF becomes ff
    c = c.lower()
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


def color_palette_inator(color_code=None):
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
        "triadic": {
            "primary": {
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
        "tetradic": {
            "primary": {
                "color": (),
                "shades": {
                    "dark": (),
                    "med-dark": (),
                    "med": (),
                    "med-light": (),
                    "light": (),
                    "lightest": (),
                },
            },
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
    if not color_code:
        primary = rgb_to_hsl(random_rgb())
    elif "#" in color_code:
        primary = hex_to_rgb(color_code)
        primary = rgb_to_hsl(primary)
    palette["primary"] = primary
    palette["background"] = get_background_from_hsl(primary)
    palette["text"] = get_text_from_hsl(primary)

    # Get triad
    triadic = get_triadic(primary)
    # use triadic colors to append colors to triadic keys
    palette["triadic"]["primary"]["color"] = triadic[0]
    set_color_shades(palette["triadic"]["primary"]["shades"], triadic[0])
    palette["triadic"]["color1"]["color"] = triadic[1]
    set_color_shades(palette["triadic"]["color1"]["shades"], triadic[1])
    palette["triadic"]["color2"]["color"] = triadic[2]
    set_color_shades(palette["triadic"]["color2"]["shades"], triadic[2])

    # Get tertiary
    tetradic = get_tetradic(primary)
    # use tetradic colors to append to tetradic keys
    palette["tetradic"]["primary"]["color"] = tetradic[0]
    set_color_shades(palette["tetradic"]["primary"]["shades"], tetradic[0])
    palette["tetradic"]["color1"]["color"] = tetradic[1]
    set_color_shades(palette["tetradic"]["color1"]["shades"], tetradic[1])
    palette["tetradic"]["color2"]["color"] = tetradic[2]
    set_color_shades(palette["tetradic"]["color2"]["shades"], tetradic[2])
    palette["tetradic"]["color3"]["color"] = tetradic[3]
    set_color_shades(palette["tetradic"]["color3"]["shades"], tetradic[3])
    return palette


def is_hex(val):
    result = False
    result = "#" in val and (len(val) == 7 or len(val) == 4)
    if not result:
        return False

    # check for proper hex digits
    for i in val:
        if i != "#" and i not in list(hex_map.keys()):
            result = False
    return result

def get_relative_luminance(val):
    val /= 255
    if val <= 0.03928:
        return val / 12.92
    else:
        return ((val + 0.055) / 1.055)**2.4
              
def luminance(rgb):
    r, g, b = rgb
    r = get_relative_luminance(r)
    g = get_relative_luminance(g)
    b = get_relative_luminance(b)
    return r * 0.2126 + g * 0.7152 + b * 0.0722
    
def contrast_ratio(hex1, hex2):
    rgb1 = hex_to_rgb(hex1)
    rgb2 = hex_to_rgb(hex2)
    l1 = luminance(rgb1)
    l2 = luminance(rgb2)
    # Make sure l1 is the lighter of the two or swap them
    if l1 < l2:
        temp = l1
        l1 = l2
        l2 = temp
    ratio = (l1 + 0.05) / (l2 + 0.05)
    # get the ratio to 2 decimal places without rounding
    # take it to 3rd decimal place, then truncate (3rd has been rounded)
    ratio = format(ratio, ".3f")[:-1]
    return float(ratio)

def get_shades(hsl, num=6):
    h, s, l = hsl
    l -= 20
    shades = []
    for i in range(num):
        shades.append((h, s, l))
        l += 10
    return shades


def get_triadic(hsl):
    h, s, l = hsl
    triad = [hsl, ]
    for i in range(2):
        h += 120
        h = h % 360
        triad.append((h, s, l))
    return triad


def get_tetradic(hsl):
    h, s, l = hsl
    tetradic = [hsl, ]
    for i in range(3):
        h += 90
        h = h % 360
        tetradic.append((h, s, l))
    return tetradic


def set_color_shades(shades, hsl):
    """ uses hsl color to set the shades """
    shade_list = get_shades(hsl)
    for pos, shade in enumerate(shades.keys()):
        shades[shade] = shade_list[pos]


if __name__ == "__main__":
    my_hex = "#336699"
    valid_hex = is_hex(my_hex)
    print(valid_hex)
    my_rgb = hex_to_rgb(my_hex)
    my_hsl = rgb_to_hsl(my_rgb)
    # print(my_hsl)
    # shades = get_shades(my_hsl)
    # print(shades)
    # triad = get_triadic(my_hsl)
    # print(triad)
    # tetradic = get_tetradic(my_hsl)
    # print(tetradic)
    # palette = color_palette_inator()
    my_palette = color_palette_inator("#336699")
    print(my_palette)
