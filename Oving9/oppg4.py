def number_of_lines(filename):
    lines = 0
    f = open(filename, 'r')
    for line in f:
        lines += 1

    return lines



def number_frequency(filename):
    number_dict= dict()
    f = open(filename, 'r')
    for line in f:
        if line[:1] not in number_dict.keys():
            number_dict[line[:1]] = 1
        else:
            number_dict[line[:1]] += 1

    return number_dict
    #lines = number_of_lines(filename)


def main():
    #print(number_of_lines('nummer.txt'))
    #print(number_frequency('nummer.txt'))

    for key, value in number_frequency('nummer.txt').items():
        print(key,': ', value, sep='')

main()
