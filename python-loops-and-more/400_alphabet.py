#!/usr/bin/python
for letter in range(ord('a'), ord('z')+1):
    if letter != ord('a') and letter != ord('q'):
        print(chr(letter), end='')
