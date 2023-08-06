# Copyright (C) 2018 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2

import os
import sys
import filecmp
import os.path
import subprocess as s

import ctypes
from ctypes import cdll
from ctypes.util import find_library


def mount(img, loc, off='1979711488'):
    """
    Mounts a dd img file to a filesystem location

    :param img The image file to be mounted
    :param loc The filesystem location to mount the image
    :param off Offset of the root filesystem
    :param default 1979711488 for the root of 16GB v4.0 Kanux

    return: 0 for success
    """
    s.run(['sudo', 'mount', '-o', 'offset=' + off, img, loc])


def load_c_library():
    """
    Loads the libc from the system to use for different calls
    like mount, etc
    """
    try:
        libc_name = find_library('c')
        libc = cdll.LoadLibrary(libc_name)
        return libc
    except:
        print('Unable to load libc.')


def mount(source, target, fs, options=''):
    """ A mount interface of the sys/mount.h from the Standard C Library
    :param source the filesystem to be attached. a path to an img, dir or a device
    :param target (pathname) the location where the source would be attached to
    :param fs the filesystem type supported by the kernel
    :param options extra options supported by the OS

    :returns 0 for Pass, -1 for Failure and sets the appropriate errno
    """
    libc = load_c_library()
    libc.mount.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_ulong, ctypes.c_char_p)

    ret = libc.mount(source, target, fs, 0, options)
    if ret < 0:
        errno = ctypes.get_errno()
        raise OSError(errno, "Error mounting {} ({}) on {} with options '{}': {}".
                      format(source, fs, target, options, os.strerror(errno)))


class dircmp(filecmp.dircmp):
    """ Comparison between contents of the files of dir1 and dir2 within the same path.
    """

    def phase3(self):
        """
            Discover the differences between common files and ensure that
            we are using content comparison with shallow=False in contrast
            with the original compare phase3 implementation.

            It does an in depth comparison of contents and doesn't rely only on os.stat() attributes

            Refer to Lib/filecmp.py of cpython
            """
        fcomp = filecmp.cmpfiles(self.left, self.right, self.common_files,
                                 shallow=False)
        self.same_files, self.diff_files, self.funny_files = fcomp


def is_same(dir1, dir2):
    """
    Compare the content of the two directory trees.
    :param dir1: Left path to compare from
    :param dir2: Right path to compare with
    :return True is they are the same or False if they differ
    """
    compared = dircmp(dir1, dir2)

    if (compared.left_only or compared.right_only or compared.diff_files
            or compared.funny_files):
        # Displays a summary report if differences are found
        compared.report_full_closure()
        return False
    for subdir in compared.common_dirs:
        if not is_same(os.path.join(dir1, subdir), os.path.join(dir2, subdir)):
            return False
    return True


def main(loc1, loc2):
    """
    The simplest user case by calling is_same()
    :param loc1: the left side path to compare from
    :param loc2: the right side path to compare with
    :return: True if they are the same, False otherwise
    """

    if os.geteuid() is not 0:
        print('Ensure that you have super user privileges.')
        sys.exit(1)

    if os.path.exists(loc1):
        if os.path.exists(loc2):
            print('Is the dir structure the same?', is_same(loc1, loc2))
        else:
            print('Directory {} doesn\'t exist'.format(loc2))
    else:
        print('Directory {} doesn\'t exist'.format(loc1))

