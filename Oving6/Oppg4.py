teeth = [95, 103, 71, 99, 114, 64, 95, 53, 97, 114, 109, 11, 2, 21, 45, 2, 26, 81, 54, 14, 118, 108, 117, 27, 115, 43, 70, 58, 107]

def coins(amount):
    total_sum = amount / 2
    
    no_20 = int(total_sum // 20)
    remainder = total_sum % 20
    no_10 = int(remainder // 10)
    remainder = remainder % 10
    no_5 = int(remainder // 5)
    remainder = remainder % 5
    no_1 = int(remainder // 1)
    remainder = remainder % 1
    no_half = int(remainder / (1/2))
    
    return no_20, no_10, no_5, no_1, no_half

def main():
    for i in teeth:
        print('Antall av hver av de ulike myntene som trengs for', i , 'gram tenner')
        print(coins(i))
        
main()