#!/usr/bin/env python

#pydog.py

import os, time, sys

def main(idata, ofile_name):
    # check if "idata" exists too, if not, assume it is a string
    # check is file is present
    if os.path.isfile(ofile_name):
        # open file to append
        file_mode = 'a'
        print('file %s is already present on file system') %ofile_name
    else:
        #open file to write
        print('creating file %s') %ofile_name
        file_mode = 'w'
    ofile = open(ofile_name, file_mode)
    ofile.write(idata)
    ofile.close()


if __name__ == "__main__":
    #sys.argv[1]
    if len(sys.argv) > 2:
        dogfile = sys.argv[2]
        ifile   = sys.argv[1]
    else:
        print("Usage:")
        print("pydog.py <string|file> <file>")
        exit(1)

    main(ifile, dogfile)
