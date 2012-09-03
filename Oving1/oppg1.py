################################
## Øving 1 - TDT4110
## Converting polar coordinates
## to carthesian coordinates.
## Øyvind Robertsen
################################
import math

pi = 3.1415

r = 3
theta = pi/2
x = r * math.cos(theta)
y = r * math.sin(theta)

print('The carthesian equivalent of ( 3 , pi/2 ) is (',x,',',y,')')

r = 2.3
theta = pi/3
x = r * math.cos(theta)
y = r * math.sin(theta)

print('The carthesian equivalent of ( 2.3 , pi/3 ) is (',x,',',y,')')

r = 5
theta = 0
x = r * math.cos(theta)
y = r * math.sin(theta)

print('The carthesian equivalent of ( 5 , 0 ) is (',x,',',y,')')
