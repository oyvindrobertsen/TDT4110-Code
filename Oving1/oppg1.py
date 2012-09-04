################################
## Øving 1 - TDT4110
## Oppgave 1
## Converting polar coordinates
## to carthesian coordinates.
## Øyvind Robertsen
################################
import math
pi = 3.1415

def convert(r, theta):
    x = format(r * math.cos(theta), '.5f')
    y = format(r * math.sin(theta), '.5f')
    theta = format(theta, '.2f')
    print('The carthesian equivalent of (',r,',',theta,') is (',x,',',y,')!')
    return

convert(3, pi/2)
convert(2.3, pi/3)
convert(5, 0)
