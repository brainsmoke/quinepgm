#!/usr/bin/env python2

# (c) 2017 Erik Bosman
# Distributed under GPLv3

import sys

chars = [ x for x in sys.stdin.readline()[1:-1].split(' ') if x != '' ]
syms  = [ x for x in sys.stdin.readline()[1:-1].split(' ') if x != '' ]

d = dict(zip(chars, syms))

code = []

for line in sys.stdin:
    ix = line.find('#')
    if ix != -1:
        line = line[:ix]

    code += [ c for c in line if c in ".<>[]+-" ]

data = [ d[c] for c in code ] + [d['END']]

data.reverse()

print ''.join( data + code )

