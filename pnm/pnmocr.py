#!/usr/bin/env python2

# Distributed under MIT Licence


import sys


patterns = {

( '0000','0010','0111','0010','0000' ) : '+',
( '0000','0000','0111','0000','0000' ) : '-',
( '0011','0010','0010','0010','0011' ) : '[',
( '0110','0010','0010','0010','0110' ) : ']',
( '0001','0011','0111','0011','0001' ) : '<',
( '0100','0110','0111','0110','0100' ) : '>',
( '0000','0000','0000','0110','0110' ) : '.',
( '1000','1100','1000','1100','1000' ) : '3',
( '0000','0000','0000','0000','0000' ) : ' ',

}

sys.stdin.readline()
sys.stdin.readline()

data = ''.join(c for c in ''.join(sys.stdin.readlines()) if c in '01')

for y in range(3, 1200-6, 6):
	for x in range(2, 100-4, 4):
		base = y*100+x
		glyph = tuple(data[base+i*100:base+i*100+4] for i in range(5))
		sys.stdout.write(patterns[glyph])
	sys.stdout.write('\n')

