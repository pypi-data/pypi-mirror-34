#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Johan Hake (hake.dev@gmail.com)"
__copyright__ = "Copyright (C) 2012-2015 " + __author__
__date__ = "2012-05-07 -- 2015-01-09"
__license__  = "GNU LGPL Version 3.0 or later"

# System imports
from setuptools import setup, Command
import os
import codecs

REQUIRE_PATH = "requirements.txt"
PROJECT      = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Assume UTF-8 encoding and return the contents of the file located at the
    absolute path from the REPOSITORY joined with *parts.
    """
    with codecs.open(os.path.join(PROJECT, *parts), 'rb', 'utf-8') as f:
        return f.read()

def get_requires(path=REQUIRE_PATH):
    """
    Yields a generator of requirements as defined by the REQUIRE_PATH which
    should point to a requirements.txt output by `pip freeze`.
    """
    for line in read(path).splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            yield line

class run_tests(Command):
    """
    Runs all tests under the modelparameters/ folder
    """

    description = "run all tests"
    user_options = []  # distutils complains if this is not here.

    def __init__(self, *args):
        self.args = args[0] # so we can pass it to other classes
        Command.__init__(self, *args)

    def initialize_options(self):  # distutils wants this
        pass

    def finalize_options(self):    # this too
        pass

    def run(self):
        import os
        os.system("python utils/run_tests.py")
        
class clean(Command):
    """
    Cleans *.pyc so you should get the same copy as is in the VCS.
    """

    description = "remove build files"
    user_options = [("all","a","the same")]

    def initialize_options(self):
        self.all = None

    def finalize_options(self):
        pass

    def run(self):
        import os
        os.system("utils/clean-files")


# Version number
major = 0
minor = 3

setup(name = "modelparameters",
      version = "{0}.{1}".format(major, minor),
      description = """
A module providing parameter structure for physical modeling
      """,
      author = __author__.split("(")[0],
      author_email = __author__.split("(")[1][:-1],
      install_requiries=list(get_requires()),
      packages = ["modelparameters", "modelparameters.tests"],
      cmdclass = {'test' : run_tests,
                  'clean' : clean,
                  },
      )
