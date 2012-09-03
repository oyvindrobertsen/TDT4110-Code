################################
## Øving 1 - TDT4110
## Oppgave 1
## Converting polar coordinates
## to carthesian coordinates.
## Øyvind Robertsen
################################
import math

pi = 3.1415

r = 3
theta = pi/2
x = format(r * math.cos(theta), '.5f')
y = format(r * math.sin(theta), '.5f')

print('The carthesian equivalent of ( 3 , pi/2 ) is (',x,',',y,')')

r = 2.3
theta = pi/3
x = format(r * math.cos(theta), '.5f')
y = format(r * math.sin(theta), '.5f')

print('The carthesian equivalent of ( 2.3 , pi/3 ) is (',x,',',y,')')

r = 5
theta = 0
x = format(r * math.cos(theta), '.5f')
y = format(r * math.sin(theta), '.5f')

print('The carthesian equivalent of ( 5 , 0 ) is (',x,',',y,')')
