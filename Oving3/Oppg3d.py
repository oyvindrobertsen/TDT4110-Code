import math


def main():
    print('Du vil nå bli spurt om areal og omkrets av sirkelen du ønsker å beregne radius til. Dersom du ønsker å beregne ved hjelp av areal, skriv inn areal (bruk . ved desimaltall), og skriv så inn 0 for omkrets. Ønsker du å bruke omkrets, skriver du den inn når den forespørres.')
    area = float(input('Areal: '))
    circumference = float(input('Omkrets: '))
    calc_rad(area, circumference)

def calc_rad(area, circumference):
    if circumference > 0:
        radius = format((circumference / (2 * math.pi)), '.2f')
        print('Radius er:', radius)
    else:
        radius = format((math.sqrt(area/math.pi)), '.2f')
        print('Radius er:', radius)

main()
