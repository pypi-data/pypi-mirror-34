# -*- coding: utf-8 -*-

# Copyright (c) 2018 Kura
# Copyright (C) 2009-2015 Barry A. Warsaw
#
# This file is part of setup_helpers.py
#
# setup_helpers.py is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, version 3 of the License.
#
# setup_helpers.py is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with setup_helpers.py.  If not, see <http://www.gnu.org/licenses/>.

"""setup.py helper functions."""

import io
import os
import sys

from setuptools.command.test import test as TestCommand


__all__ = ('get_version', 'include_file', 'require_python', 'PyTest')


class PyTest(TestCommand):
    """Test command."""

    def finalize_options(self):
        """Build options."""
        TestCommand.finalize_options(self)
        self.test_args = ['--pylama', '-q', './blackhole', './tests']
        self.test_suite = True

    def run_tests(self):
        """Run ze tests."""
        import pytest
        sys.exit(pytest.main(self.test_args))


def require_python(minimum):
    """Python version check."""
    if sys.hexversion < minimum:
        hversion = hex(minimum)[2:]
        if len(hversion) % 2 != 0:
            hversion = '0' + hversion
        split = list(hversion)
        parts = []
        while split:
            parts.append(int(''.join((split.pop(0), split.pop(0))), 16))
        major, minor, micro, release = parts
        if release == 0xf0:
            print('Python {0}.{1}.{2} or higher is required'.format(
                major, minor, micro))
        else:
            print('Python {0}.{1}.{2} ({3}) or higher is required'.format(
                major, minor, micro, hex(release)[2:]))
        sys.exit(1)


def include_file(filename):
    """Include contents of specified file."""
    fpath = os.path.join(os.path.dirname(__file__), filename)
    with io.open(fpath, encoding='utf-8') as f:
        c = f.read()
    return c


def get_version(filepath):
    """Return program version."""
    for line in include_file(filepath).split('\n'):
        if line.startswith('__version__'):
            _, vers = line.split('=')
            return vers.strip().replace('"', '').replace("'", '')
