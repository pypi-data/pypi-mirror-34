# Copyright 2018 Alexandru Catrina
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os

from buildok.util.log import Log


WORKING_DIR = os.getcwd()
LOCK_FILE = os.path.join(WORKING_DIR, ".build.lock")


def lock():
    """Create a lock file.

    Raises:
        SystemExit: If a lock file already exists.
    """

    if os.path.isfile(LOCK_FILE):
        raise SystemExit("A build might be launched by another process")
    with open(LOCK_FILE, "a"):
        os.utime(LOCK_FILE, None)
        Log.info("Created temporary lock")


def unlock():
    """Releases a lock file.

    Raises:
        OSError: If lock file cannot be released.
    """

    if os.path.isfile(LOCK_FILE):
        os.remove(LOCK_FILE)
        Log.info("Removed temporary lock")
