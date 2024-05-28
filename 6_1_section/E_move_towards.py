from math import dist, cos, sin

x, y = map(float, input().split())
p, phi = map(float, input().split())

print(dist((x, y), (p * cos(phi), p * sin(phi))))