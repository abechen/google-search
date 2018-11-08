from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

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
    install_requires              = [
        "bs4==0.0.1",
        "requests==2.19.1"
    ],
    classifiers                   = [
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7"
    ],
    keywords                      = ["google", "search"],
    entry_points                  = {}
)