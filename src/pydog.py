#!/usr/bin/env python

#pydog.py

import os, time, sys

#sys.argv[1]
if len(sys.argv) != 1:
  dogfile = sys.argv[2]
  ifile   = sys.argv[1] 
  # check is file is present
  if os.path.isfile(dogfile):
    # open file to append
    print()
  else:
    #open file to write
    #dogfile = open(
    print()
  print("I'll do lots of things")

else:
  print("Usage:")
  print("pydog.py <string|file> <file>")
