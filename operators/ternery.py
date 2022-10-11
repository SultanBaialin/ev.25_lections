# sentence = input('Vvedite predlogenie:')

# if sentence[-1] == '?':
#     print('предложение вопросительное')
# else:
#     print('Обычное предложение')

# sentence = input('Vvedite predlogenie:')
# print('Предложение вопросительное' if sentence[-1] == '?' else 'Обычное предложение')
# -------------------------------------------------
# Ternary operator(Тернарный оператор) - коонструкция, которая аналогична по ссвоим свойствам и действию конструкции if/else, но при этом записывается в одну строчку
# <выражение если в условии True> if <условие> else <выражение есои False>

# number = 15 
# res = 'even' if number % 2 == 0 else 'odd number'
# print(res)

# from string import digits

# symbols = digits + '-'
# print(symbols)
# number = input('Vvedite chislo: ')
# is_correct = True
# for i in number: #567
#     if i not in symbols: #0123456789-
#          is_correct = False

# if is_correct:
#     print('yes number')
#     number = int(number) 
#     print('Your number:', number)
#     result = number if number >= 0 else -number
#     print(result)
# else:
#     print('Invalid values!')         
#


# if number.isdigit():
#     number = int(number)
#     print('Да число!')
# else:
#     print('Вы вывели не число!')

# ---------------------------------------------------------------------------------

from string import digits

flag = True 
symbols = digits + '-' + '.'

while flag:
    is_correct_number = True
    num1 = input('Vvedite pervoe chislo: ')

    if len(num1) <= 1 and (num1 == '.' or num1 == '-') or not num1:
        print('Вы ввели неправильное число!')
        is_correct_number = False

    for x in num1:
        if x not in symbols:
            print('Вы ввели неправильное число!')
            is_correct_number = False
            break
    if not is_correct_number:
        continue    

    num2 = input('Vvedite vtoroe chislo: ')

    if len(num2) <= 1 and (num2 == '.' or num2 == '-') or not num2:
        print('Вы ввели неправильное число!')
        is_correct_number = False

    for x in num2:
        if x not in symbols:
            print('Вы ввели неправильное число!')
            is_correct_number = False
            break

    if not is_correct_number:
        continue       
    num1 = float(num1) if '.' in num1 else int(num1)
    num2 = float(num2) if '.' in num2 else int(num2)
    operator = input('Vvedite operator(+, -, *, /): ')

    if operator == '+': 
        print(f'Result: {num1 + num2}')
    elif operator == '-': 
        print(f'Result: {round(num1 - num2, 2)}')
    elif operator == '*': 
        print(f'Result: {num1 * num2}')
    elif operator == '/': 
        if num2 == 0:
            print('На ноль делить нельзя')
        else:
            print(f'Result: {round(num1 / num2, 2)}')
    else:
        print('Вы ввели не правельный оператор!!')
    
    choice = input('Хотите остановить (yes): ')
    if choice.lower() == 'yes':
        flag = False
        print('Пока!')
        



