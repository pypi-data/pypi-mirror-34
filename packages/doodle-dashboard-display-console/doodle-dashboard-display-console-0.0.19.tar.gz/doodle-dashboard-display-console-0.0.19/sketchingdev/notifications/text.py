import textwrap

from sketchingdev.notifications.centre import centre_in_container


def format_text(size, notification):
    text = notification.get_text()
    width = size[0]
    height = size[1]

    wrapped_lines = textwrap.wrap(text, width)
    cropped = wrapped_lines[:height]

    centred = centre_in_container(cropped, size)

    return "\n".join(centred)
