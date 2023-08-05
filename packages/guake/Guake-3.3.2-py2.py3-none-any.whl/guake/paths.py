# -*- coding: utf-8; -*-
"""
Copyright (C) 2007-2013 Guake authors

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 2 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public
License along with this program; if not, write to the
Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
Boston, MA 02110-1301 USA
"""

from pkg_resources import Requirement
from pkg_resources import resource_filename
import guake
import logging
import os
import sys

log = logging.getLogger(__name__)


def get_default_package_root():
    packagedir = guake.__path__[0]
    dirname = os.path.join(os.path.dirname(packagedir))
    return os.path.abspath(dirname)


def get_data_files_dir():
    d = os.path.dirname(sys.modules["guake"].__file__)
    p = os.path.basename(os.path.abspath(os.path.join(d, "..")))
    # print("p", p)
    if p in ["site-packages", "dist-packages"]:
        # current "guake" package has been installed in a prefix structure (/usr, /usr/local or
        # ~/.local/)
        loc_dir = os.path.abspath(os.path.join(d, "..", "..", "..", ".."))
        loc_dir = os.path.join(loc_dir, "share", "guake")
        # print("loc_dir", loc_dir)
        if os.path.exists(loc_dir):
            return loc_dir
    return d


def get_default_data_dir():
    d = os.path.join(get_data_files_dir(), "data")
    print("Using guake data directory: {}".format(d))
    return d


def get_default_locale_dir():
    d = os.path.join(get_data_files_dir(), "po")
    print("Using guake image directory: {}".format(d))
    return d


def get_default_image_dir():
    d = os.path.join(get_default_data_dir(), 'pixmaps')
    print("Using guake image directory: {}".format(d))
    return d


def get_default_glade_dir():
    d = get_default_data_dir()
    print("Using guake glade directory: {}".format(d))
    return d


def get_default_schema_dir():
    d = get_default_data_dir()
    print("Using guake scheme directory: {}".format(d))
    return d


def get_default_theme_dir():
    d = os.path.join(get_default_data_dir(), 'theme')
    print("Using guake theme directory: {}".format(d))
    return d


LOCALE_DIR = get_default_locale_dir()
IMAGE_DIR = get_default_image_dir()
GLADE_DIR = get_default_glade_dir()
SCHEMA_DIR = get_default_schema_dir()
GUAKE_THEME_DIR = get_default_theme_dir()
LOGIN_DESTOP_PATH = ""
AUTOSTART_FOLDER = ""


def try_to_compile_glib_schemas():
    import subprocess
    subprocess.check_call(["glib-compile-schemas", "--strict", SCHEMA_DIR])
