def csv_to_dict(filename):
    limit_dict = dict([(l.split(",")[0], l.split(",")[1]) for l in open(filename, 'r')])

    for key, value in limit_dict.items():
        limit_dict[key] = value.strip('"\n')
        limit_dict[key.strip('"')] = limit_dict.pop(key)

    return limit_dict

def no_limit(dictionary):
    i = 0
    for l in dictionary:
        if dictionary[l] == 'Alle' or dictionary[l] == '"Alle"\n':
            i += 1
    return i

def average_limit(dictionary):
    total = 0
    items = 0

    for i in dictionary:
        if dictionary[i] != 'Alle' and dictionary[i] != '"Alle"\n':
            total += float(dictionary[i])
            items += 1

    return total/items


def high_low_limit(dictionary):
    high = 0
    low = 0

    for i in dictionary:
        if dictionary[i] != 'Alle' and dictionary[i] != '"Alle"\n':
            if high == 0:
                high, low = dictionary[i]
            elif dictionary[i] < low:
                low = dictionary[i]
            elif dictionary[i] > high:
                high = dictionary[i]

    high_low_tuple = high, low
    return high_low_tuple

def main():
    #print(csv_to_dict('poenggrenser_2011.csv'))
    print(no_limit(csv_to_dict('poenggrenser_2011.csv')))
    print(average_limit(csv_to_dict('poenggrenser_2011.csv')))
    print(high_low_limit(csv_to_dict('poenggrenser_2011.csv')))

main()
