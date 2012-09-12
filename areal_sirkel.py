import math

def areal_sirkel(r, pi):
    A = pi*pow(r,2)
    print('Radius: ',r,', areal: ',A,'.',sep='')

def main():
    r = eval(input('Tast inn sirkelens radius: '))
    areal_sirkel(r, math.pi)

main()
