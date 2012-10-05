def gcd(a,b):

    while b > 0:
        gammel_b = b
        b = a % b
        a = gammel_b

    return a

def reduce_fraction(c,d):

    assert type(c) != 'int', "%r er ikke et heltall!" % c
    assert type(d) != 'int', "%r er ikke et heltall!" % d

    a = gcd(c,d)
    c = c / a
    d = d / a
    return c,d


def main():
    e,f = reduce_fraction(5,10)
    print(int(e) ,'/',int(f) , sep='')
    e,f = reduce_fraction(4,2)
    print(int(e) ,'/',int(f) , sep='')
    e,f = reduce_fraction(42,13)
    print(int(e) ,'/',int(f) , sep='')


main()
