"""whratio setuptools file"""

from setuptools import setup
import whratio

setup(
    name       = whratio.__name__,
    version    = whratio.__version__,
    py_modules = ["whratio"],

    author       = whratio.__author__,
    author_email = whratio.__email__,
    description  = whratio.__doc__,
    license      = whratio.__license__,
    keywords     = "calculate aspect ratio dimension width height image video",
    url          = "https://github.com/mirukan/whratio",

    entry_points = {
        "console_scripts": [
            "whratio=whratio:main"
        ]
    },

    classifiers=[
        "Development Status :: 5 - Production/Stable",

        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",

        "Environment :: Console",

        "Topic :: Utilities",

        "License :: OSI Approved :: GNU Lesser General Public License v3 "
        "or later (LGPLv3+)",

        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",

        "Natural Language :: English",

        "Operating System :: POSIX",
    ]
)
