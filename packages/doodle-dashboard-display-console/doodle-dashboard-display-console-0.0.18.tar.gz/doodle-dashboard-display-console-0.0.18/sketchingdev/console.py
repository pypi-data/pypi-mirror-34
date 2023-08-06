import click
from doodledashboard.configuration.config import ConfigSection
from doodledashboard.display import Display
from doodledashboard.notifications import TextNotification, ImageNotification

from sketchingdev.notifications.image import format_image
from sketchingdev.notifications.text import format_text


class ConsoleDisplay(Display):

    _NOTIFICATIONS = {
        TextNotification: format_text,
        ImageNotification: format_image
    }

    def __init__(self, size=click.get_terminal_size()):
        self._size = size

    def draw(self, notification):
        click.clear()
        factory = self.find_factory(notification)
        click.echo(factory(self._size, notification), nl=False)

    def find_factory(self, notification, default=lambda x, y: ""):
        for factory_type, factory in self._NOTIFICATIONS.items():
            if isinstance(notification, factory_type):
                return factory

        return default

    @staticmethod
    def get_supported_notifications():
        return ConsoleDisplay._NOTIFICATIONS.keys()

    @staticmethod
    def get_id():
        return "console"

    def __str__(self):
        return "Console display"

    @staticmethod
    def get_config_factory():
        return ConsoleConfig()


class ConsoleConfig(ConfigSection):

    @property
    def id_key_value(self):
        return "display", "console"

    def create(self, config_section):
        return ConsoleDisplay()
