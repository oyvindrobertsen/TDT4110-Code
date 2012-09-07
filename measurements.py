maling1 = float(input('Første måling: '))
maling2 = float(input('Andre måling: '))
maling3 = float(input('Tredje måling: '))
snitt = format((maling1+maling2+maling3)/3, '.4f')
print('Snittet av målingene:', snitt,'.')


def add(a, b):
    c = a + b
    return c

p = add(2, 4)

print('The value of p is',p,)
