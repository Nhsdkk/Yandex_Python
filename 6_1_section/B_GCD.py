from sys import stdin
from math import gcd

for line in stdin.readlines():
    items = map(int, line.split())
    print(gcd(*items))