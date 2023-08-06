# coding=utf-8
# Inspired from snips-nlu: https://github.com/snipsco/snips-nlu
from __future__ import unicode_literals

import logging
import sys

import plac

from diggers_toolbox.cli.conversion import convert_directory
from diggers_toolbox.cli.utils import PrettyPrintLevel, pretty_print

logger = logging.getLogger("diggers_toolbox")

logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

logger.addHandler(handler)


def main():
    commands = {
        "convert-directory": convert_directory,
    }
    if len(sys.argv) == 1:
        pretty_print(', '.join(commands), title="Available commands", exits=1,
                     level=PrettyPrintLevel.INFO)
    command = sys.argv.pop(1)
    sys.argv[0] = 'snips-nlu %s' % command
    if command in commands:
        plac.call(commands[command], sys.argv[1:])
    else:
        pretty_print("Available: %s" % ', '.join(commands),
                     title="Unknown command: %s" % command, exits=1,
                     level=PrettyPrintLevel.INFO)


if __name__ == "__main__":
    main()
