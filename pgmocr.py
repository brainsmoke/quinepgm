#!/usr/bin/env python2

# (c) 2017 Erik Bosman
# Distributed under GPLv3

import sys

w, h = sys.argv[1:]
w, h = int(w), int(h)

patterns = {

    ( '001100','001100','111111','111111','001100','001100' ) : '+',
    ( '000000','000000','111111','111111','000000','000000' ) : '-',
    ( '011110','011000','011000','011000','011000','011110' ) : '[',
    ( '011110','000110','000110','000110','000110','011110' ) : ']',
    ( '000110','001100','011000','011000','001100','000110' ) : '<',
    ( '011000','001100','000110','000110','001100','011000' ) : '>',
    ( '000000','000000','000000','000000','001100','001100' ) : '.',

}
assert (sys.stdin.readline() == 'P5\n')
assert (sys.stdin.readline() == str(w)+' '+str(h)+'\n')
assert (sys.stdin.readline() == '255\n')

data = ''.join(str(int(c!='\0')) for c in sys.stdin.read() )

assert(len(data) == w*h)

for y in range(2, h-6, 7):
    for x in range(2, w-6, 7):
        base = y*w+x
        glyph = tuple(data[base+i*w:base+i*w+6] for i in range(6))
        sys.stdout.write(patterns[glyph])
    sys.stdout.write('\n')

