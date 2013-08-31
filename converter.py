#!usr/bin/env python

import os, sys

input = open(sys.argv[1])
output = open(sys.argv[2], 'w')

subs = input.read().decode("Windows-1250")
output.write(subs.encode('utf-8'))

output.close()
input.close()
