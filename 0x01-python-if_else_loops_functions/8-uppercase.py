#!/usr/bin/python

def uppercase(str,value=0):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            value = 32
        else:
            value = 0
        print('{:c}'.format(ord(i) - value), end='')
    print()