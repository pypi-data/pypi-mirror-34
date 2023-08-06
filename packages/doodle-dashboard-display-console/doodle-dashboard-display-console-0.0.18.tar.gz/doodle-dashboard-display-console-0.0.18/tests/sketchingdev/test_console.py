import click
import unittest
from click.testing import CliRunner

from sketchingdev.console import ConsoleDisplay


class TestConsoleDisplay(unittest.TestCase):

    def test_id(self):
        self.assertEqual("console", ConsoleDisplay().get_id())

    def test_nothing_drawn_for_unsupported_notifications(self):
        image_notification = None
        cmd = create_cmd(lambda: ConsoleDisplay().draw(image_notification))
        result = CliRunner().invoke(cmd, catch_exceptions=False)

        self.assertEqual("", result.output)


def create_cmd(func):
    @click.command()
    def c(f=func):
        f()

    return c


if __name__ == "__main__":
    unittest.main()
