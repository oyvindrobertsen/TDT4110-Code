def main():
    fahrenheit = int(input('Skriv inn grader fahrenheit: '))
    konverter(fahrenheit)

def konverter(fahrenheit):
    celsius = format(((fahrenheit - 32) * (5/9)), ".2f")
    print(fahrenheit,'grader i fahrenheit er', celsius,' grader i celsius')

main()
