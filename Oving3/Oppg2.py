debug = True

def main():
    x = int(input('Skriv inn et heltall: '))
    y = int(input('Skriv inn et heltall til: '))
    add(x, y)

def add(x, y):
    z = x + y
    if debug == True:
        print('Tallene som summeres:', x, y)
        print('Summen er:', z)
    else:
        print('Summen er:', z)

main()
