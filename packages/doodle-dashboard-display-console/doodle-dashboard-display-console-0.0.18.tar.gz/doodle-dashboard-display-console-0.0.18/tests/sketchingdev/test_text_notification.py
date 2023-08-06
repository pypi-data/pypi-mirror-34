import click
import unittest
from click.testing import CliRunner
from doodledashboard.notifications import TextNotification
from parameterized import parameterized

from sketchingdev.console import ConsoleDisplay
from tests.sketchingdev.terminal.ascii_terminal import AsciiTerminal


class TestConsoleDisplayWithText(unittest.TestCase):

    @parameterized.expand([
        ((1, 1), "",
         """
         +-+
         ||
         +-+
         """),
        ((10, 3), "a",
         """
         +----------+
         ||
         |    a|
         ||
         +----------+
         """),
        ((10, 3), "centred",
         """
         +----------+
         ||
         | centred|
         ||
         +----------+
         """),
        ((10, 3), "I'm centred",
         """
         +----------+
         |   I'm|
         | centred|
         ||
         +----------+
         """),
        ((10, 3), "Hello World! This is too long",
         """
         +----------+
         |  Hello|
         |  World!|
         | This is|
         +----------+
         """),
    ])
    def test_text_centred_in_console(self, console_size, input_text, expected_ascii_terminal):
        expected_terminal = AsciiTerminal.extract_text(expected_ascii_terminal)

        text_notification = TextNotification()
        text_notification.set_text(input_text)
        cmd = create_cmd(lambda: ConsoleDisplay(console_size).draw(text_notification))
        result = CliRunner().invoke(cmd, catch_exceptions=False)

        self.assertEqual(expected_terminal, result.output)


def create_cmd(func):
    @click.command()
    def c(f=func):
        f()

    return c


if __name__ == "__main__":
    unittest.main()
