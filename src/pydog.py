#!/usr/bin/env python

#pydog.py

import os, time, sys

def main(text, ofile_name):
    # check is file is present
    if os.path.isfile(ofile_name):
        # open file to append
        file_mode = 'a'
    else:
        #open file to write
        file_mode = 'w'
    ofile = open(ofile_name, file_mode)
    ofile.close()

    print("I'll do lots of things")


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
