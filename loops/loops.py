# Циклы - это конструкция при помощи которых можно оргазизовать многократное исполнение определенного кода 

# while <expression>:
#     <body>
# <else>:
#      <body>

# i = 1
# while i <= 10:
#     print(f'Цикл выполнился{i} раз!')
#     i += 1
# else:
#     print('End!')


# name1 = ''
# name2 = ''
# i = 0 

# while name1.lower() != 'john' and name2.lower() != 'jamie':
#     name1 = input('VVEDITE IMYA1: ')
#     name2 = input('VVEDITE IMYA2: ')
#     i += 1 
#     if i > 4:
#         print('Цикл остановлен!!!')
#         break
# else:
#     print('Vy vveli pravilnoe imya!')

# admin = ['johnsnow23', 'ilovepython23']
# i = 3
# username = None
# password = None 

# while username != admin[0] or password != admin[1]:
#     username = input('Vvedite username: ')
#     password = input('Vvedite password: ')
#     i -= 1
#     if i == 0:
#         print('Vy zablokirovany na 5 min!')
#         break
# else:
#     print(f'{admin[0]} vy uspeshno zashli v sistemu!')

#======================================================

# for <variable> in <iterable object>:
#     <body>

# list_ = [0, 1, 2, 3, 4, 5]
# i = iter(list_)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# for x in list_:
#     print(x)
#============================================================\

# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# for x in ls:
#     print(f'Element: {x}') 

# i = 0
# while i < len(ls):
#     print(f'Element: {ls[i]}') 
#     i += 1

#============================================================

# secret_list = ['DeltaViski', 'LOTR123', 'JohnSnow']
# word = input('Enter secret code: ')

# while word not in secret_list:
#     print('incorrect word! Try one more time!')
#     word = input('Enter secret code: ')
# print(f'You\'re welcom my friend, {word}!')

#=============================================================\

#1
# steps = 8 
# path = 'UDDDUDUU'
# res = 1 

# #2
# # steps  = 9 
# # path = 'UDDUUDDUU'
# # res = 2

# sea_level = 0 
# dolina = 0
# for x in path:
#     if x == 'U':
#         sea_level += 1
#         if sea_level == 0:
#             dolina += 1
#     elif x == 'D':
#         sea_level -= 1 

# print(dolina)                 
 
   






lists = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# summa = 0
# for num in lists:
#   if num == float:
#     summa += num

word_list = lists.split()
num_list = []
 
for word in word_list:
    if word.isnumeric():
        num_list.append(int(word))
 
print(num_list)






















