# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить
# случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a'
# до 'f' включительно.


import random

a = int(input('Введите начальную границу для поиска целого числа'))
b = int(input('Введите конечную границу для поиска целого числа'))
print('Случайное целое число в интервале от {} до {} = {}'.format(a, b, random.randint(a, b)))

a = float(input('Введите начальную границу для поиска вещественного числа'))
b = float(input('Введите конечную границу для поиска вещественного числа'))
print('Случайное целое число в интервале от {} до {} = {}'.format(a, b, random.uniform(a, b)))

a = input('Введите начальный символ для поиска случайного символа в интервале')
b = input('Введите начальный символ для поиска случайного символа в интервале')
abc_list = 'abcdefghijklmnopqrstuvwxyz'
a_index = abc_list.index(a)
b_index = abc_list.index(b)
c = abc_list[random.randint(a_index, b_index)]
print('Случайный символ в интервале от {} до {} = {}'.format(a, b, c))
