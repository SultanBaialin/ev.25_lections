# print(dir(str)) #методы строк 

# replace(old, new, [count]) - меняем в строке old на new значение, если вы укажите count,  то он заменит его ровно count раз. 

# text = 'ha ha ha ha'
# result = text.replace('a','i',2)
# print(text)
# print(f'result after replace: {result}')

# str1 = 'Hello world! My name is John Snow'
# res = str1.replace('John', 'Jamie')
# res
# print(res)

# print(id('H'))
# print(id('H'))
# print(id('h'))

# strip() - убирает пробельные символы в начале и в конце сткроки 
# # rstrip, lstrip

# text = input('Enter the text:')
# print(text)
# print(len(text))
# res = text.strip()
# print(res)
# print(len(res))
# texr ='hello world'
# len(text)
# res = (text.rstrip)
# print(len(res))

# isdigit -.>   проверяют 
# inmumeric -> состоит ли наша строка
# isdemical -> полностью из чисел

# text = '5a'
# if text.isdigit():
#     num = int(text)
#     print(num)
# else:    
#     print('Oops! Invalid symbol!')

# text = '\u0030'
# print(text)
# print(text.isnumeric())

# isalnum() -> проверяет состоит ли наша строка из чисел и символов латинского алфавита и киррилицы

# str1 = '56a'
# print(str1.isalnum())
# str2 = '56_a'
# print(str2.isalnum())

# isalpha() ->  состоит ли наша строка полностью из символов латинского либо киррильского алфавитов
 
# text = 'Helloworld'
# print(text[:5].isalpha())

# islower() 
# isupper()
# istitle()

# index(value, [start], [end]) ->  выводит индекс значения  value  которое мы передаем в нашей строке.

# count(value, [start]) -> считает количество вхождений value  в нашу строку

# text = 'hello o o hello'
# print(text.count('hello'))
# print(text.count('o'))
# print(text.count(' '))

# text = 'Hello world! My name is John Snow'
# print(text.index('John'))
# print(text.index('o', 5))
# print(text[24])

# text = 'Hello world! My name is John Snow'
# print(text.index('John'))
# res = text.index('o')
# print(res)
# res = text.index('o', res+1)
# print(res)
# res = text.index('o', res+1)
# print(res)
# res = text.index('o', res+1)
# print(res)

# text = 'oooHello world! Myo name is John Snowooo'
# text = input('Enter the text:')
# i = 0
# res = -1
# while i < text.count('o'):
#     res = text.index('o', res+1)
#     print(res)
#     i += 1   #инкремент

# find(value, [start], [end]) -> делает то же самое что и index, но есть одно отличие, в том что если value нет в строке то возвращает индекс -1 

# text = 'Hello'
# print(text.find('l'))
# print(text.find('hi'))

# swapcase() -> Переводит все символы в противоположный регистр
# upper() -> все символы в верхний регистр
# lower() -> все символы в нижний регистр 

# text = 'Hello world, JoHN, SNow'
# print(text)
# print(text.swapcase())
# print(text.upper())
# print(text.lower())

# capitalize() - переводит первую букву в верхний регистр 

# name = input('Enter your name:').capitalize()
# print(f'Hello mr/mrs {name}!')

# title() -> переводит первые символы всех слов в верхний регистр
# text = 'john jamie sansa nursultan jerri'
# print(text)
# print(text.title())
# print(text.capitalize())

# split(разделитель) - дробит строку на несколько частей по разделителю который находится в строке, все части строки сохраняются в типе данных list 

# text = 'Let me speak by my heart in English! Cause My name is John Snow!'
# ls = text.split(' ')
# print(ls)
# print(len(ls))

# 'разделитель'.join(iterable(list)) -> соединяет по разделителю строки, которые находятся в list

# res = ' '.join(ls)
# print(res)






