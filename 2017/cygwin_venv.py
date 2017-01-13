#!/usr/bin/env python

"""Cygwin venv

This script adds a posix activate script to a Windows Python virtual
environment.

  Usage: ./cygwin_venv.py VENV_DIR

"""

import os
import venv
import subprocess
import sys

def convert_path(windows_path):
    """Convert a windows path to a Cygwin unix path"""
    return subprocess.check_output(['cygpath.exe', '--unix', windows_path]).decode('utf-8').strip()

def main(env_dir):
    """Add a posix 'activate' script to a virtual environment for Cygwin"""
    env_dir = os.path.abspath(env_dir)

    builder = venv.EnvBuilder()
    context = builder.ensure_directories(env_dir)
    context.env_dir = convert_path(context.env_dir)

    activate_path = os.path.join(context.bin_path, 'activate')
    if os.path.exists(activate_path):
        print('Script already exists: "%s"' % activate_path)
        return

    venv_path = os.path.abspath(os.path.dirname(venv.__file__))
    template = os.path.join(venv_path, 'scripts', 'posix', 'activate')

    with open(activate_path, 'w', newline='') as activate_file:
        with open(template, 'r') as activate_tpl:
            activate_file.write(builder.replace_variables(activate_tpl.read(), context))
    print('Created: "%s"' % activate_path)

if __name__ == '__main__':
    if len(sys.argv) == 2 and os.path.isdir(sys.argv[1]):
        main(sys.argv[1])
    else:
        print(__doc__)
