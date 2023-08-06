import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="cnpt_leos",
    version="0.1.1",
    author = "Dmitry Obukhov",
    author_email = "bstodin@gmail.com",
    description = ("Custom NLTK part of speech tagger"),
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
