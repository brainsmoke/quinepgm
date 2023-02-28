#!/usr/bin/env python2

# Distributed under MIT Licence

import sys

chars = [ x for x in sys.stdin.readline()[1:-1].split(' ') if x != '' ]
syms  = [ x for x in sys.stdin.readline()[1:-1].split(' ') if x != '' ]

d = dict(zip(chars, syms))
d['#'] = ''

code = []

for line in sys.stdin:
	ix = line.find('#')
	if ix != -1:
		line = line[:ix]

	line=line.replace('%','#')
	code += [ c for c in line if c in ".<>[]+-#3~" ]

data = [ d[c] for c in code ] + [d['NULL']]

data.reverse()

quine = ''.join( data + code ).replace('~',' ')

for i in range(0, len(quine)-24, 24):
	print quine[i:i+24]

