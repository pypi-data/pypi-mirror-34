# coding=utf-8
from __future__ import unicode_literals

import logging
import shutil
from contextlib import contextmanager

from future.builtins import str

try:
    from tempfile import TemporaryDirectory
except ImportError:
    from backports.tempfile import TemporaryDirectory

logger = logging.getLogger(__name__)


@contextmanager
def copy_to_dir_if_success(output_path):
    with TemporaryDirectory() as tmp_dir:
        logger.info("Created tmp directory %s to proceed to conversion ",
                    tmp_dir)
        yield tmp_dir
        logger.info("Moving %s to final directory %s", tmp_dir, output_path)
        shutil.copytree(str(tmp_dir), str(output_path))


def suffix_to_ext(suffix):
    return suffix[1:]
