# coding=utf-8
from __future__ import unicode_literals

import logging
import os
from pathlib import Path

from pydub import AudioSegment
from pydub.utils import mediainfo
from tqdm import tqdm

from diggers_toolbox.utils import copy_to_dir_if_success, suffix_to_ext

logger = logging.getLogger(__name__)

DEFAULT_BITRATES = {
    "mp3": "320"
}


def _get_file_tags(file_path):
    return mediainfo(str(file_path)).get("TAG", {})


def _convert_file(input_path, output_path, source_extension, target_extension):
    input_ext = suffix_to_ext(input_path.suffix)
    if source_extension != input_ext:
        logger.warning("Input path does not have correct extension, expected "
                       "%s found: %s", source_extension, input_ext)
    output_ext = suffix_to_ext(output_path.suffix)
    if target_extension != output_ext:
        logger.warning("Output path does not have correct extension, expected "
                       "%s found: %s", target_extension, output_ext)
    input_audio = AudioSegment.from_file(str(input_path), source_extension)
    input_tags = _get_file_tags(input_path)
    input_audio.export(str(output_path), format=target_extension,
                       bitrate=DEFAULT_BITRATES[target_extension],
                       tags=input_tags)


def convert_file(input_path, output_path):
    input_path = Path(input_path)
    output_path = Path(output_path)
    source_extension = suffix_to_ext(input_path.suffix)
    target_extension = suffix_to_ext(output_path.suffix)
    logging.info("Converting %s to %s", input_path, output_path)
    _convert_file(input_path, output_path, source_extension, target_extension)


def convert_dir(input_dir, output_dir, source_ext, target_ext):
    with copy_to_dir_if_success(output_dir) as tmp_dir:
        files_to_convert = []
        for root, _, files in os.walk(str(input_dir)):
            root = Path(root)
            for f in files:
                input_file = root / f
                if suffix_to_ext(input_file.suffix) != source_ext:
                    continue
                files_to_convert.append(input_file)

        for input_file in tqdm(files_to_convert):
            target_name = "%s.%s" % (input_file.stem, target_ext)
            tmp_file = Path(tmp_dir) / target_name
            convert_file(input_file, tmp_file)
