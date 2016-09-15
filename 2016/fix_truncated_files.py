#!/usr/bin/env python

""" Rename truncated files extracted from an ISO using TRANS.TBL files. """

import os
import sys

def check_paths(dir_path, rename=False):
    """Check for files missing files

    Check for missing file that exist in TRANS.TBL. If rename is set to true
    truncated files will be renamed to match TRANS.TBL entries.

    """
    trans_file = os.path.join(dir_path, 'TRANS.TBL')

    files = os.listdir(dir_path)

    if not os.path.exists(trans_file):
        raise FileNotFoundError('Missing TRANS.TBL file in %s' % dir_path)

    with open(trans_file, 'r') as trans_table:
        for line in trans_table.readlines():
            full_name = line.split(' ')[-1].strip()
            full_path = os.path.join(dir_path, full_name)
            if not os.path.exists(full_path):
                print('Missing file: %s' % full_name)
                if rename:
                    matches = [filename for filename in files if full_name.startswith(filename)]
                    if len(matches) == 1:
                        old_path = os.path.join(dir_path, matches[0])
                        print('Renaming: %s -> %s' % (old_path, full_path))
                        os.rename(old_path, full_path)

def main(paths):
    """Rename trunctaed files in specified directories"""
    for path in paths:
        if not os.path.isdir(path):
            raise FileNotFoundError('%s does not exist!' % path)
        for dirpath, _, _ in os.walk(path):
            check_paths(dirpath, rename=True)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        main(sys.argv[1:])
    else:
        print('Usage: %s PATH...' % sys.argv[0])
        show_help()
