#!/usr/bin/env python3
#
# bf interpreter

# (c) 2018 Erik Bosman
# Distributed under MIT Licence

import sys

m=[0]*1000000

code = open(sys.argv[1],'r').read()
xrefs = [None] * len(code)

s=[]
for i,c in enumerate(code):
    if c == '[':
        s.append(i)
    elif c == ']':
        if s == []:
            s = ["unbalanced"]
            break
        xrefs[i] = s.pop()      # xrefs for the loop [] pairs
        xrefs[xrefs[i]] = i     #

if s != []:
    sys.stderr.write('Unbalanced braces\n')
    sys.exit(1)

pc = 0
p = 0
while pc < len(code):
    inst = code[pc]
    if inst == '>':
        p += 1
    elif inst == '<':
        p -= 1
    elif inst == '[':
        if m[p] == 0:
            pc = xrefs[pc]
    elif inst == ']':
        if m[p] != 0:
            pc = xrefs[pc]
    elif inst == '+':
        m[p] = (m[p]+1)%256
    elif inst == '-':
        m[p] = (m[p]-1)%256
    elif inst == '.':
        sys.stdout.buffer.write(bytes([m[p]]))
    elif inst == ',':
        m[p] == ord(sys.stdout.buffer.read(1))
    pc += 1

