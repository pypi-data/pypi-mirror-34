"""
distutilazy.pyinstaller
-----------------------
command classes to call pyinstaller

:license: MIT. For more details see LICENSE file or
https://opensource.org/licenses/MIT
"""

from __future__ import absolute_import

import os
import platform
import subprocess
from distutils.core import Command
from distutils.errors import DistutilsOptionError

from . import clean

__version__ = "0.3.0"

is_windows = platform.system().upper() == "WINDOWS"
path_separator = is_windows and ';' or ':'


class BdistPyInstaller(Command):
    """Distutils command to run PyInstaller with configured defaults"""

    description = "Run PyInstaller to create standalone executable programs"

    user_options = [
        ("target=", 't', "Target Python app to bundle"),
        ("pyinstaller-path=", None, "Path to PyInstaller executable"),
        ("name=", 'n', "Name of the bundled app"),
        ("icon=", 'i', "Path to icon resource"),
        ("windowed", 'w', "Windowed app, no console for stdio"),
        ("clean", None, "Clean cached and temp files before build"),
        ("hidden-imports=", 'I',
            "comma separated list of extra modules to be imported"),
        ("paths=", 'p',
         "extra paths to search for modules separated by '{}'".format(
             path_separator)
         ),
    ]

    boolean_options = ["windowed", "clean"]

    def initialize_options(self):
        self.pyinstaller_opts = []
        self.imports = []
        self.syspaths = []
        self.target = None
        self.pyinstaller_path = None
        self.name = None
        self.icon = None
        self.windowed = None
        self.clean = None
        self.hidden_imports = None
        self.paths = None

    def default_pyinstaller_opts(self):
        """Return default options for PyInstaller.
        Use this method to customize the command for separate projects

        :return: list of options
        """
        return ["--onefile"]

    def default_imports(self):
        """Return list of explicit imports.
        Use this method to customize the extra modules for separate projects

        :return: list of module names to be imported
        """
        return []

    def default_paths(self):
        """Return list of paths to append to sys.path while importing modules.
        Use this method to customize the extra paths for separate projects

        :return: list of paths
        """
        return []

    def finalize_options(self):
        if self.pyinstaller_path:
            self.pyinstaller_path = os.path.abspath(self.pyinstaller_path)
            if not os.path.exists(self.pyinstaller_path):
                raise DistutilsOptionError(
                        "failed to find pyinstaller from '{}'".format(
                            self.pyinstaller_path)
                    )
        self.pyinstaller_opts.extend(self.default_pyinstaller_opts())
        if not self.name:
            self.name = self.distribution.metadata.get_name()
        if self.clean:
            self.pyinstaller_opts.append("--clean")
        if self.windowed:
            self.pyinstaller_opts.append("--windowed")
        if self.icon:
            self.pyinstaller_opts.append("--icon=" + self.icon)
        if not is_windows:
            self.pyinstaller_opts.append("--strip")

        self.imports.extend(self.default_imports())
        if self.hidden_imports:
            self.imports.extend(
                [i.strip() for i in self.hidden_imports.split(',')
                 if i.strip()]
            )
        for module in self.imports:
            self.pyinstaller_opts.append("--hidden-import=" + module)

        self.syspaths.extend(self.default_paths())
        if self.paths:
            self.syspaths.extend(
                [p for p in self.paths.split(path_separator)]
            )
        for path in self.syspaths:
            self.pyinstaller_opts.append("--paths=" + path)
        self.pyinstaller_opts.append("--name=" + self.name)

    def run(self):
        if not self.target:
            raise DistutilsOptionError("no target app is specified to bundle")
        py_installer = self.pyinstaller_path or "pyinstaller"
        args = self.pyinstaller_opts
        args.append(self.target)
        args.insert(0, py_installer)
        self.announce("running " + ' '.join(args))
        code = subprocess.call(args)
        return code


class CleanAll(clean.CleanAll):
    """Distutils command to clean all temporary files,
    compiled Python files, PyInstaller temp files and spec.
    """

    user_options = [
        ("keep-build", None, "do not clean build directory"),
        ("keep-dist", None, "do not clean dist directory"),
        ("keep-egginfo", None, "do not clean egg info directory"),
        ("keep-extra", None, "do not clean extra files"),
        ("name", None, "name of the bundled app"),
    ]

    def initialize_options(self):
        clean.CleanAll.initialize_options(self)
        self.name = None

    def finalize_options(self):
        clean.clean_all.finalize_options(self)
        if not self.name:
            self.name = self.distribution.metadata.get_name()

    def get_extra_paths(self):
        """Return list of extra files/directories to be removed"""
        return [self.name + ".spec"]


bdist_pyinstaller = BdistPyInstaller
clean_all = CleanAll
