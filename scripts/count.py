#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2018 Slightech Co., Ltd. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function

import os
import sys
import re


def ishan(ch):
  return u'\u4e00' <= ch <= u'\u9fff'


def iter_msgids(filepath):
  with open(filepath, 'r') as f:
    is_msgid = False
    for l in f.readlines():
      m = re.match('msgid "(.*)"', l.rstrip())
      if m:
        msgid = m.group(1)
        if msgid:
          yield msgid
        is_msgid = True

      if is_msgid:
        m = re.match('"(.*)"', l.rstrip())
        if m:
          msgid = m.group(1)
          if msgid:
            yield msgid

      if l.startswith('msgstr'):
        is_msgid = False


def count_hans(filepath):
  count = 0
  for msgid in iter_msgids(filepath):
    n = 0
    for ch in msgid:
      if ishan(ch):
        n = n + 1
    count = count + n
    # print('%s %d/%d' % (msgid, n, count))
  return count


def _parse_args():
  import argparse
  parser = argparse.ArgumentParser(
      prog=os.path.basename(__file__),
      formatter_class=argparse.RawTextHelpFormatter,
      description='usage examples:'
      '\n  python %(prog)s -p PATH')
  parser.add_argument(
      '-p',
      '--path',
      dest='path',
      metavar='PATH',
      required=True,
      help='the directory path of po files')
  return parser.parse_args()


def _main():
  args = _parse_args()

  path = args.path
  if not os.path.exists(path):
    sys.exit('Error: the path not exists, %s' % path)
  if not os.path.isdir(path):
    sys.exit('Error: the path is not a directory, %s' % path)

  print('The directory path: %s' % path)
  print()

  chapters = {}
  count = 0
  for root, dirs, files in os.walk(path):
    if not files: continue
    files = [f for f in files if os.path.splitext(f)[1] == '.po']
    if not files: continue
    # print(root)
    sections = []
    for f in files:
      hans_n = count_hans(os.path.join(root, f))
      sections.append((f, hans_n))
      # print('  %s %d' % (f, hans_n))
      count = count + hans_n
    chapters[root] = sections

  for k, v in chapters.items():
    print(k)
    for f, n in v:
      print('{:30s} {:6d} {:6.2f}%'.format(f, n, (n / count) * 100))

  print('\nhans count: %d' % count)


if __name__ == '__main__':
  _main()
