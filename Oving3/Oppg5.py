def main ():
    a = int(input('Skriv inn a: '))
    b = int(input('Skriv inn b: '))
    c = int(input('Skriv inn c: '))
    decide(a,b,c)

def decide(a,b,c):
    d = (b ** 2) - 4 * a * c
    if d < 0:
        print('Andregradslikningen din har 2 imaginære løsninger.')
    elif d > 0:
        print('Andregradslikningen din har 2 reelle løsninger.')
    elif d == 0:
        print('Andregradslikningen din har 1 reell løsning.')
    else:
        print('You dun goofd.')

main()
