# coding=utf-8
from __future__ import unicode_literals

from setuptools import find_packages, setup

packages = [p for p in find_packages() if "test" not in p]

requires = [
    "backports.tempfile; python_version < '3.4'",
    "future>=0.16.0<0.17",
    "pathlib>=1.0,<2.0; python_version < '3.4'",
    "plac>=1.0,<2.0",
    "pydub>=0.22,<0.23",
    "tqdm>=4.0<5.0"
]

extras_require = {
    "tests": [
        "pytest>=3.7,<4.0",
        "pylint>=1.0,<2.0",
    ]
}
setup(
    name="DiggersToolbox",
    version="0.1.0",
    author="Clément Doumouro",
    author_email="clement.doumouror@gmail.com",
    description="Toolbox for music diggers",
    packages=packages,
    install_requires=requires,
    extras_require=extras_require,
    entry_points={
        "console_scripts": [
            "diggers-toolbox=diggers_toolbox.__main__:main"
        ]
    },
)
