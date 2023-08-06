from PIL import Image
from sketchingdev.notifications.centre import centre_in_container

GREYSCALE_CHARS = ['@', '%', '#', '*', '+', '=', '-', ':', ',', '.', ' ']
GREYSCALE_CHARS_MAX_INDEX = len(GREYSCALE_CHARS) - 1
ELEMENT_RANGE = element_range = GREYSCALE_CHARS_MAX_INDEX / 255


def map_pixel_to_character(pixel):
    char_index = int(ELEMENT_RANGE * pixel)
    return GREYSCALE_CHARS[char_index]


def convert_to_grayscale(image):
    return image.convert('L')


def convert_image_to_ascii(image):
    image = convert_to_grayscale(image)

    width, height = image.size
    pixels = list(image.getdata())
    rows = [pixels[i * width:(i + 1) * width] for i in range(height)]

    ascii_rows = []
    for row in rows:
        textual_row = "".join([map_pixel_to_character(pixel) for pixel in row])

        ascii_rows.append(textual_row)

    return ascii_rows


def format_image(size, notification):
    image_path = notification.get_image_path()

    try:
        image = Image.open(image_path)
    except Exception:
        return "ERROR\nUnable to open image: %s" % notification.get_image_path()

    image.thumbnail(size, Image.ANTIALIAS)
    ascii_image = convert_image_to_ascii(image)
    centred_image = centre_in_container(ascii_image, size)

    return "\n".join(centred_image).rstrip("\n")
