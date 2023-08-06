import re


class ValidationError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class AsciiTerminal:
    """
    Provides a convenient way of representing the terminal as text in the tests e.g. a terminal of 5x5 is represented
    as:

    +-----+
    |     |
    |     |
    |     |
    |     |
    |     |
    +-----+
    """

    _WIDTH_REGEX = re.compile("\s*\+([-]+)\+")

    @staticmethod
    def _strip_chars_outside_terminal_border(target_lines):
        spaces_stripped = map(lambda x: x.strip(" "), target_lines)
        non_empty = filter(lambda l: len(l) > 0, spaces_stripped)
        return list(non_empty)

    @staticmethod
    def _validate(lines):
        def any_filtered(filter_func, items):
            results = list(filter(filter_func, items))
            return len(results) > 0

        if len(lines) < 2:
            raise ValidationError("ASCII terminal must contain at width indicator at top and bottom")

        if not AsciiTerminal._WIDTH_REGEX.match(lines[0]):
            raise ValidationError("First line must be a width indicator")

        if not AsciiTerminal._WIDTH_REGEX.match(lines[-1]):
            raise ValidationError("Last line must be a width indicator")

        if len(lines) > 2:
            console_lines = lines[1:-1]

            if any_filtered(lambda line: len(line) < 2, console_lines):
                raise ValidationError("All lines between width indicators contain at least two pipes")

            if any_filtered(lambda line: line[0] != "|", console_lines):
                raise ValidationError("All lines between width indicators must start with a pipe")

            if any_filtered(lambda line: line[-1] != "|", console_lines):
                raise ValidationError("All lines between width indicators must end with a pipe")

    @staticmethod
    def _remove_border(lines):
        without_width_indicators = lines[1:-1]
        without_pipes = map(lambda line: line[1:-1], without_width_indicators)
        text = "\n".join(list(without_pipes))
        return text.rstrip("\n")

    @staticmethod
    def extract_text(text):
        lines = text.split("\n")
        cleaned = AsciiTerminal._strip_chars_outside_terminal_border(lines)
        AsciiTerminal._validate(cleaned)
        return AsciiTerminal._remove_border(cleaned)
