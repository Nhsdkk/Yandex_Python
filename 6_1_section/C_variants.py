from math import comb

n, k = map(int, input().split())
print(comb(n, k) * k // n, comb(n, k))