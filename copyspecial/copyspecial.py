#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

# Returns a list of the absolute paths of the special files in the given directory
def get_special_paths(dir):
  filenames = os.listdir(dir)
  absolutepaths = []

  for filename in filenames:
    match = re.search('\w*__\w+__.*', filename)
    if match:
      absolutepaths.append(os.path.abspath(match.group()))

  return absolutepaths

def copy_to(paths, dir):
  absdir = os.path.abspath(dir)

  if not os.path.exists(absdir):
    os.mkdir(absdir)

  for path in paths:
    basename = os.path.basename(path)
    shutil.copy(path, os.path.join(absdir, basename))

  return

def zip_to(paths, zippath):
  files = ' '.join(paths)

  cmd = 'zip -j ' + zippath + ' ' + files
  try:
    print "Command I'm going to do: " + cmd
    err = os.system(cmd)
  except IOError:
    sys.stderr.write('problem reading:' + filename)

  return


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  if todir:
    copy_to(get_special_paths(args[1]), todir)
  elif tozip:
    zip_to(get_special_paths(args[1]), tozip)
  else:
    print '\n'.join(get_special_paths(args[1]))
  
if __name__ == "__main__":
  main()
