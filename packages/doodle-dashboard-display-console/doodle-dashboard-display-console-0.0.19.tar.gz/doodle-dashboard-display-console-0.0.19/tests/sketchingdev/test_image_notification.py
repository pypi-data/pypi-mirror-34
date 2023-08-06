import click
import os
import unittest
from click.testing import CliRunner
from doodledashboard.notifications import ImageNotification
from os import path
from parameterized import parameterized

from sketchingdev.console import ConsoleDisplay
from tests.sketchingdev.terminal.ascii_terminal import AsciiTerminal


def _get_current_directory():
    return os.path.dirname(os.path.realpath(__file__))


def resolve_data_path(filename):
    data_dir = path.join(_get_current_directory(), "data/")
    return path.join(data_dir, filename)


class TestConsoleDisplayWithImages(unittest.TestCase):

    @parameterized.expand([
        ((10, 10), resolve_data_path("cross-without-transparency.png"),
         """
         +----------+
         |   @@@%   |
         |   @@%#   |
         |   @%##   |
         |@@@%##*=-:|
         |@@%##*=-::|
         |@%##*=-::,|
         |%##*=-::,.|
         |   =-::   |
         |   -::,   |
         |   ::,.   |
         +----------+
         """),
        ((10, 10), resolve_data_path("cross-with-transparency.png"),
         """
         +----------+
         |   @@@%   |
         |   @@%#   |
         |   @%##   |
         |@@@%##*=-:|
         |@@%##*=-::|
         |@%##*=-::,|
         |%##*=-::,.|
         |   =-::   |
         |   -::,   |
         |   ::,.   |
         +----------+
         """),
        ((12, 12), resolve_data_path("cross-without-transparency.png"),
         """
         +-----------+
         ||
         |    @@@%   |
         |    @@%#   |
         |    @%##   |
         | @@@%##*=-:|
         | @@%##*=-::|
         | @%##*=-::,|
         | %##*=-::,.|
         |    =-::   |
         |    -::,   |
         |    ::,.   |
         ||
         +-----------+
         """),
        ((10, 10), resolve_data_path("rgb-with-transparency.png"),
         """
         +----------+
         |          |
         | ####==== |
         | ####==== |
         | ####==== |
         | ####==== |
         |   ####   |
         |   ####   |
         |   ####   |
         |   ####   |
         |          |
         +----------+
         """),
        ((10, 5), resolve_data_path("3x3-box.png"),
         """
         +----------+
         ||
         |   @@@|
         |   @@@|
         |   @@@|
         ||
         +----------+
         """)
    ])
    def test_text_centred_in_console(self, console_size, input_image, expected_ascii_terminal):
        expected_terminal = AsciiTerminal.extract_text(expected_ascii_terminal)

        image_notification = ImageNotification()
        image_notification.set_image_path(input_image)
        cmd = create_cmd(lambda: ConsoleDisplay(console_size).draw(image_notification))
        result = CliRunner().invoke(cmd, catch_exceptions=False)

        self.assertEqual(expected_terminal, result.output)


def create_cmd(func):
    @click.command()
    def c(f=func):
        f()

    return c


if __name__ == "__main__":
    unittest.main()
