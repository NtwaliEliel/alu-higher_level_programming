#!/usr/bin/python3
import sys
number = 3.14159
print(f"Float: {number:,.2f}")
sys.stderr = open('err.txt', 'w')
print("[Anything", file=sys.stderr)
