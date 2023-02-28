#!/usr/bin/env python2
#
# bf to c translator

# (c) 2017 Erik Bosman
# Distributed under GPLv3

import sys

memsize="1000000"

tr = {

    '.': 'putchar(m[p]);',
    ',': 'm[p] = getchar();',
    '>': 'p++;if (p >= '+memsize+') abort();',
    '<': 'p--;if (p < 0) abort();',
    '-': 'm[p]--;',
    '+': 'm[p]++;',
    '[': 'while(m[p]){',
    ']': '}',
}

code = sys.stdin.read()

b=0
for c in code:
    if c == '[':
        b+=1
    elif c == ']':
        b-=1
        if b < 0:
            break

if b != 0:
    sys.stderr.write('Unbalanced braces\n')
    sys.exit(1)

print """
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(void) {
char m["""+memsize+"""];
memset(m,0,sizeof(m));
long p=0;"""

for c in code:
    if c in ".,<>[]+-":
        print tr[c]

print "}"

