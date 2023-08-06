"""
distutilazy.util
----------------
utility functions

:license: MIT. For more details see LICENSE file or
https://opensource.org/licenses/MIT
"""

import os
import fnmatch


def find_files(root, pattern):
    """Find all files matching the glob pattern recursively

    :param root: string
    :param pattern: string
    :return: list of file paths relative to root
    """
    results = []
    for base, dirs, files in os.walk(root):
        matched = fnmatch.filter(files, pattern)
        results.extend(os.path.join(base, f) for f in matched)
    return results


def find_directories(root, pattern):
    """Find all directories matching the glob pattern recursively

    :param root: string
    :param pattern: string
    :return: list of dir paths relative to root
    """
    results = []
    for base, dirs, files in os.walk(root):
        matched = fnmatch.filter(dirs, pattern)
        results.extend(os.path.join(base, d) for d in matched)
    return results
