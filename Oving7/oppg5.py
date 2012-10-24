def equal_strings(string1, string2):
    i = 0
    if len(string1) == len(string2):
        for x in string2:
            if x == string1[i]:
                i += 1
            else:
                return False

        return True

    else:
        return False


def reverse_string(string):
    return_string = []

    for x in reversed(range(len(string))):
        return_string.append(string[x])

    return ''.join(return_string)



def palindrome(string):
    if len(string)&1 == 0:
        first_half = ''.join([string[i] for i in range(len(string)//2)])
        second_half = ''.join([string[i] for i in reversed(range(len(string)//2))])

        if equal_strings(first_half, reverse_string(second_half)):
            return True
        else:
            return False
    else:
        return False

def stringception(string1, string2):
    if string1.find(string2) == -1:
        return False
    else:
        return True




def main():
    print(equal_strings("test", "test"))
    print(reverse_string("humonculus"))
    print(palindrome("abba"))
    print(stringception("pappa", "ap"))

main()
