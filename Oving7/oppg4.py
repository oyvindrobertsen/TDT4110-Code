def is_prime(x):
    for i in range(2, x):
        if x%i==0:
            return False
        else:
            pass
    return True

def separate(numbers, threshold):
    list1 = []
    list2 = []

    for i in numbers:
        if i >= threshold:
            list2.append(i)
        else:
            list1.append(i)

    return list1, list2

def multiplication_table(n):
    return [[j * i for i in range(1, n + 1)] for j in range(1, n + 1)]
    # multiplication_table() kan også implementeres med nøstede for-løkker.

def main():
    print(is_prime(int(input('Skriv inn et heltall: '))), '\n')
    print('================================================\n')
    print(separate(list(range(200)), 50), '\n')
    print('================================================\n')
    print(multiplication_table(3))

main()
