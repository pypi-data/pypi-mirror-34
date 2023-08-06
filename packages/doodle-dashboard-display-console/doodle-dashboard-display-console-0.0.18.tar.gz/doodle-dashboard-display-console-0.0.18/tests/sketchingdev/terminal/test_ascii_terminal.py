import pytest
import unittest

from tests.sketchingdev.terminal.ascii_terminal import ValidationError, AsciiTerminal


class AsciiTerminalTests(unittest.TestCase):

    def test_validation_fails_if_first_line_not_width_indicator(self):
        text_terminal = """

        |A
        +-+
        """

        with pytest.raises(ValidationError) as err_info:
            AsciiTerminal.extract_text(text_terminal)

        self.assertEqual("First line must be a width indicator", err_info.value.value)

    def test_validation_fails_if_last_line_not_width_indicator(self):
        text_terminal = """
        +-+
        |A
        """

        with pytest.raises(ValidationError) as err_info:
            AsciiTerminal.extract_text(text_terminal)

        self.assertEqual("Last line must be a width indicator", err_info.value.value)

    def test_validation_fails_if_lines_between_width_indicators_do_not_start_with_pipe(self):
        text_terminal = """
                +-+
                 A
                +-+
                """

        with pytest.raises(ValidationError) as err_info:
            AsciiTerminal.extract_text(text_terminal)

        self.assertEqual("All lines between width indicators contain at least two pipes", err_info.value.value)

    def test_validation_fails_if_lines_between_width_indicators_does_not_end_with_pipe(self):
        text_terminal = """
                +-+
                |A
                +-+
                """

        with pytest.raises(ValidationError) as err_info:
            AsciiTerminal.extract_text(text_terminal)

        self.assertEqual("All lines between width indicators must end with a pipe", err_info.value.value)

    def test_get_text_returns_single_line_text(self):
        text_terminal = """
                +----+
                |   A|
                +----+
                """

        terminal = AsciiTerminal.extract_text(text_terminal)
        self.assertEqual("   A", terminal)

    def test_get_text_returns_multiline_text(self):
        text_terminal = """
                +----+
                |   A|
                |  B|
                +----+
                """

        terminal = AsciiTerminal.extract_text(text_terminal)
        self.assertMultiLineEqual("   A\n  B", terminal)

    def test_get_text_returns_multiline_text_without_trailing_whitespace(self):
        text_terminal = """
                +----+
                |   A|
                |  B|
                ||
                +----+
                """

        terminal = AsciiTerminal.extract_text(text_terminal)
        self.assertEqual("   A\n  B", terminal)
