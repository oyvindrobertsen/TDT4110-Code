def lfib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def rfib(n):
    if n < 2:
        return n
    else:
        return rfib(n-1) + rfib(n-2)

def listfib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b

def main():
    print(lfib(44))
    print(rfib(4))
    print(listfib(5))

main()
