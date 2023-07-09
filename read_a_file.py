#!/usr/bin/python
open_file=open('poem.txt')
for line in open_file.readlines():
    print(line, end='')
