# age = int(input('Введите Ваш возраст '))
# if age > 18:
#     print('OK')
# if age == 18:
#     print('ТЫ УЖЕ СЧИТАЕШСЯ ВЗРОСЛЫМ')
# if age < 17:
#     print('NO')

# print(1 > 0)
# print(1 < 0)
# if '34' > "120":
#     print('OK')
# if 1 > 0:
#     print('OK')
# if [2, 2] >= [2, 1]:
#     print('OK')
# if [2, 2] <= [2, 1]:
#     print('OK')
# if [2, 2] == [2, 1]: # == равно
#     print('OK')
# if [2, 2] != [2, 1]: # != не равно
#     print('OK')

# a = 10
# if a > 1 and a < 10: # and - строгий оператор
#     print('OK')
# if a > 1 or a < 10: # or - не строгий оператор
#     print('OK')
# a = 10
# if a == 5 and (a > 1 or a < 10):
#     print('OK')
# a = 10
# if '2' > a: # - not supported between instances of 'str' and 'int'
#     print('OK')

a, b = 10, 5
if a > b:
    print('a > b')
if a > b and a > 0:
    print('успех')
if (a > b) and (a > 0 or b < 1000):
    print('успех')
if 5 < b and b < 10:
    print('успех')

if '31' > '123':
    print('успех')
if '123' > '12':
    print('успех')
if [1, 2] > [1, 1]:
    print('успех')

if '6' > 5:
    print('успех')
if [5, 6] > 5:
    print('успех')
if '6' != 5:
    print('успех')