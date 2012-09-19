def price_calc(age):
    if age < 6 or age > 60:
        print('Gratis')
    elif 5 <= age <= 15:
        print('10 kr')
    elif 16 <= age <= 20:
        print('20 kr')
    elif 21 <= age <=25:
        print('30 kr')
    elif 26 <= age <= 60:
        print('40 kr')

price_calc(15)
price_calc(3)
price_calc(19)
price_calc(22)
price_calc(40)
price_calc(87)
