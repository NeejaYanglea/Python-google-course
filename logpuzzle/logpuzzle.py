#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import operator

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  f = open(filename, 'r')

  paths = re.findall(r'GET (.*puzzle.*) HTTP', f.read())
  pathset = set(paths)
  pathlist = sort_list(pathset)

  return pathlist

def sort_list(unsorted_set):
  sorted_list = []
  support_list = []

  for item in unsorted_set:
    match = re.search('-\w+-(\w+).jpg', item)
    if match:
      support_list.append((item, match.group(1)))
  if support_list == []:
    sorted_list = sorted(unsorted_set)
  else:
    support_list.sort(key=operator.itemgetter(1))
    sorted_list = [a for (a,b) in support_list]

  return sorted_list


def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)
  
  if os.listdir(dest_dir) == []:
    for i, url in enumerate(img_urls):
      complete_url = 'http://code.google.com' + url
      print 'Retrieving image from ' + complete_url
      urllib.urlretrieve(complete_url, os.path.join(dest_dir, 'img' + str(i) + '.jpg'))

  page = open(dest_dir + '.html', 'w+')
  page.write('<html>\n<body>\n')
  images = os.listdir(dest_dir)
  images.sort(key=natural_keys)

  for image in images:
    page.write('<img src="' + os.path.join(dest_dir, image) + '">')
  
  page.write('\n</body>\n</html>')
  page.close()

#helper functions for natural sorting
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)', text) ]

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])


  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
