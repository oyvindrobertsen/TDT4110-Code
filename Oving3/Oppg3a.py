import math

def circle_properties(r):
    area = format((math.pi * pow(r,2)), '.2f')
    circumference = format((2 * math.pi * r), '.2f')
    print('Areal:', area)
    print('Omkrets:', circumference)

def main():
    circle_properties(int(input('Skriv inn radius av sirkelen:')))

main()
