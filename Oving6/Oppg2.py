li = [1, 2, 3, 4, 5, 6]

def multiply():
    for i, j in enumerate(li):
        if j % 2 == 0:
            li[i] = li[i] * -1

    return


def main():

    multiply()
    li.sort()

    for i in li:
        print(i)

main()
