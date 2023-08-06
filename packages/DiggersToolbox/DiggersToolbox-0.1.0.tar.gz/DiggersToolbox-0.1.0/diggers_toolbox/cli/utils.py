# Copied from snips-nlu: https://github.com/snipsco/snips-nlu
from __future__ import print_function, unicode_literals

import sys
from enum import Enum, unique


@unique
class PrettyPrintLevel(Enum):
    INFO = 0
    WARNING = 1
    ERROR = 2
    SUCCESS = 3


def pretty_print(*texts, **kwargs):
    """Print formatted message
    Args:
        *texts (str): Texts to print. Each argument is rendered as paragraph.
        **kwargs: 'title' becomes coloured headline. exits=True performs sys
        exit.
    """
    exits = kwargs.get("exits")
    title = kwargs.get("title")
    level = kwargs.get("level", PrettyPrintLevel.INFO)
    title_color = _color_from_level(level)
    if title:
        title = "\033[{color}m{title}\033[0m\n".format(title=title,
                                                       color=title_color)
    else:
        title = ""
    message = "\n\n".join([text for text in texts])
    print("\n{title}{message}\n".format(title=title, message=message))
    if exits is not None:
        sys.exit(exits)


def _color_from_level(level):
    if level == PrettyPrintLevel.INFO:
        return "92"
    if level == PrettyPrintLevel.WARNING:
        return "93"
    if level == PrettyPrintLevel.ERROR:
        return "91"
    if level == PrettyPrintLevel.SUCCESS:
        return "92"
    raise ValueError("Unknown PrettyPrintLevel: %s" % level)
