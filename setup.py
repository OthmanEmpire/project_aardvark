# TODO:
# Add a run server command class
# Add the DEC10 commands for installing PyQT + Django + Sphinx
# Report CleanCommand bug that states files are missing when deleting
# Report CleanCommand bug directory is not empty


"""
A script that allows automated project management (Python's solution to a
MAKEFILE).

The main commands of interest are located within the setup argument,
under cmdclass option.

Also for more details, checkout the README.md file within the project for
further instructions of use.
"""

import os
import subprocess
import shutil
import webbrowser

import sys
from sys import platform as _platform

from setuptools import setup, find_packages, Command
from setuptools.command.install import install


def readme():
    """
    Opens the README file and returns it's contents
    :return: String content of README file
    """
    with open("README.md") as file:
        return file.read()


class RunClientCommand(Command):
    """
    A command class to runs the client GUI.
    """
    description = "runs client gui"
    # The format is (long option, short option, description).
    user_options = [
        ('socket=', None, 'The socket of the server to connect (e.g. '
                          '127.0.0.1:8000'),
    ]

    def initialize_options(self):
        """
        Sets the default value for the server socket.
        """
        self.socket = '127.0.0.1:8000'

    def finalize_options(self):
        """
        Overriding a required abstract method.
        """
        pass

    def run(self):
        """
        Semantically, runs 'python src/client/view.py SERVER_SOCKET' on the
        command line.
        """
        print(self.socket)
        errno = subprocess.call([sys.executable,
                                 'src/client/view.py ' + self.socket])
        if errno != 0:
            raise SystemExit("Unable to run client GUI!")


class PyTestCommand(Command):
    """
    A command class to run tests.
    """
    description = "runs all tests"
    user_options = []

    def initialize_options(self):
        """
        Overriding a required abstract method.
        """
        pass

    def finalize_options(self):
        """
        Overriding a required abstract method.
        """
        pass

    def run(self):
        """
        Semantically, runs 'python test/run_tests.py' on the command line.
        """
        errno = subprocess.call([sys.executable, 'test/run_tests.py'])
        if errno != 0:
            raise SystemExit("Unable to run tests or some tests failed!")


class CleanCommand(Command):
    """
    A command class to clean the current directory (removes folders).
    """
    description = "cleans the project directory"
    user_options = []

    def initialize_options(self):
        """
        Overriding a required abstract method.
        """
        pass

    def finalize_options(self):
        """
        Overriding a required abstract method.
        """
        pass

    def run(self):
        """
        Deletes some folders that can be generated (cross-platform).
        """
        ignoreDirs = ["src", "test", "doc", ".git", ".idea"]
        ignoreFiles = [".gitignore", ".gitlab-ci.yml", "README.md", "setup.py"]


        deleteDirs = [dir for dir in os.listdir(".")
                      if dir not in ignoreDirs and os.path.isdir(dir)]

        deleteFiles = [file for file in os.listdir(".")
                       if file not in ignoreFiles and os.path.isfile(file)]

        for file in deleteFiles:
            os.remove(file)

        for dir in deleteDirs:
            shutil.rmtree(dir)

        errno = subprocess.call('cd doc && make clean', shell=True)
        if errno != 0:
            raise SystemExit("Unable to clean docs!")


class GenerateDocCommand(Command):
    """
    A command class to generate the code documentation.
    """
    description = "generates project documentation"
    user_options = []

    def initialize_options(self):
        """
        Overriding a required abstract method.
        """
        pass

    def finalize_options(self):
        """
        Overriding a required abstract method.
        """
        pass

    def run(self):
        """
        Generates the project documentation.
        """
        errno = subprocess.call('cd doc && make clean && make html', shell=True)

        if errno != 0:
            raise SystemExit("Unable to generate docs!")


class RunDocCommand(Command):
    """
    A command class to open the documentation in the default browser.
    """
    description = "opens documentation in browser"
    user_options = []

    def initialize_options(self):
        """
        Overriding a required abstract method.
        """
        pass

    def finalize_options(self):
        """
        Overriding a required abstract method.
        """
        pass

    def run(self):
        """
        Opens the project documentation in a browser.
        """
        relativePath = 'doc/build/html/index.html'
        webbrowser.open('file://' + os.path.realpath(relativePath))


class InstallInVirtualEnv(install):
    """
    A command class to install the project in a virtual environment
    (cross-platform).
    """

    def run(self):
        """
        Setups up the virtual environment, activates it and then installs the
        project and it's dependencies (cross-platform).
        """
        errno1 = subprocess.call('virtualenv venv', shell=True)

        if _platform == "win32":
            errno2 = subprocess.call('activate', shell=True)

        elif _platform == "linux" or _platform == "linux2":
            errno2 = subprocess.call('source venv/bin/activate', shell=True)

        install.run(self)

        if errno1 != 0:
            raise SystemExit("Unable to setup the virtual environment!")
        if errno1 != 0:
            raise SystemExit("Unable to activate the virtual environment!")


setup(
    name='team_aardvark_restaurant',
    version='1.0',
    packages=find_packages(),

    install_requires=['requests', 'Sphinx', 'pdoc'],
    test_suite="tests",

    cmdclass={
        'runInstall': InstallInVirtualEnv,
        'runClient': RunClientCommand,
        'runTests': PyTestCommand,
        'runClean': CleanCommand,
        'generateDoc': GenerateDocCommand,
        'runDoc': RunDocCommand,
    },

    author='Team Aardvark',
    author_email='sc14omsa@leeds.ac.uk',
    description='Restaurant Booking And Billing System (Client-Server)',
    long_description=readme(),
    url='https://gitlab.com/comp2541/aardvark',
    classifiers=[
        "Programming Language :: Python :: 3.4",
        "Topic :: Management :: Restaurant"
    ],
)


# def generateCommand(command_subclass):
#     """
#     A decorator method that returns a standard class template for classes
#     that inherit from setuptools command class.
#
#     Specifically, it overrides the abstract methods required for a setuptools
#     command class without adding any functionality.
#     """
#
#     orig_run = command_subclass.run
#     orig_initialize = command_subclass.initialize_options
#     orig_finalize = command_subclass.finalize_options
#
#     def modified_initialize_options(self):
#         """
#         Overrides the empty abstract method.
#
#         The original method is responsible for setting default values for
#         all the options that the command supports.
#
#         In practice, this is used as a lazy constructor.
#         """
# #        orig_initialize(self)
#         pass
#
#     def modified_finalize_options(self):
#         """
#         Overrides the empty abstract method.
#
#         The original method is responsible for setting and checking the final
#         values for all the options just before the method run is executed.
#
#         In practice, this is where the values are assigned and verified.
#         """
# #        orig_finalize(self)
#         pass
#
#     def modified_run(self):
#        """
#        Overrides the default run method but doesn't add any additional
#        functionality yet.
#        """
#        orig_run(self)
#
#    command_subclass.initialize_options = modified_initialize_options
#    command_subclass.finalize_options = modified_finalize_options
#    command_subclass.run = modified_run
#
#    return command_subclass