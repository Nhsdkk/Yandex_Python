items = [item for item in map(float, input().split())]
res = 1
for item in items:
    res *= item

print(res ** (1 / len(items)))
