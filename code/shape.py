#!/usr/bin/env python

import sys

for line in sys.stdin:
        line = line.strip()
        keys =line.split("\t")
        if keys[3]!='':
                print (keys[3] + "\t1")
