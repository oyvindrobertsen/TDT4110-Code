def sum_series(n):
    add = 0
    for y in range(1, n):
        if (add > (n - y ** 2)):
            break
        add += y ** 2
    return add


def main():
    print(sum_series(int(input('Skriv inn et heltall n: '))))

main()
