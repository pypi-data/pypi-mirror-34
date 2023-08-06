# coding=utf-8
from __future__ import unicode_literals

from future.builtins import str

import plac

from diggers_toolbox import convert_dir


@plac.annotations(
    input_dir=("Path to the directory to convert", "positional", None, str),
    output_dir=("Target path for the converted directory", "positional", None,
                str),
    source_ext=("Source extension", "positional", None, str, ["mp3", "flac"]),
    target_ext=("Target extension", "positional", None, str, ["mp3", "flac"]))
def convert_directory(input_dir, output_dir, source_ext, target_ext):
    convert_dir(input_dir, output_dir, source_ext, target_ext)
