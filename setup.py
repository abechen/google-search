import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [
    "bs4==0.0.1",
    "requests==2.19.1"
]
test_requirements = [
    "pytest>=3.7.4"
]

about = {}

setup(
    name                          = "google-search",
    version                       = "1.0",
    author                        = "Abe Chen",
    author_email                  = "abe.chen723@gmail.com",
    description                   = "",
    long_description              = long_description,
    long_description_content_type = "text/markdown",
    url                           = "https://github.com/abechen/google-search",
    packages                      = find_packages(),
    python_requires               = ">=2.7",
    install_requires              = requirements,
    classifiers                   = [
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7"
    ],
    keywords                      = ["google", "search"],
    entry_points                  = {},
    cmdclass                      = {"test": PyTest},
    tests_require                 = test_requirements
)