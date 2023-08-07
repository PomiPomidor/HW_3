#Задание 1. Ввести предложение, состоящие из двух слов. Поменять местами слова, добавить восклицательный знак в начало и конец,
# разделить слова 3 символами, вывести итоговое предложение на экран. Сделать это тремя способами
import random

# word1 = input('Enter the first word: ')
# word2 = input('Enter the second word: ')
#
# string2 = '{1} {0}'.format(word1, word2)
# string1 = '{} {}'.format(word2, word1)
# print(f'!{string1}', sep=' ! ', end = '! \n')
# print(f'!{string2}', sep=' ! ', end = '! \n')
# print(f'!{word2} {word1}', sep=' ! ', end = '! \n')

#почему-то не работает сепаратор, но я не понял, что сделал неправильно



#Задание 4 основное. Ввести целое число n. Получить сумму кубов всех целых чисел от 1 до n (включая n). Реализовать
#через while и через for

# n = int(input('Enter number: '))
# lst = []
# for i in range(n+1):
#     i = i ** 3
#     lst.append(i)
# sum_lst = sum(lst)
# print(sum_lst)

# n = int(input('Enter number: '))
# lst = []
# a = 0
# while a <= n:
#     cube = a ** 3
#     a += 1
#     lst.append(cube)
# sum_lst = sum(lst)
# print(sum_lst)


# Задание 5 основное. Сделать программу, в которой нужно будет угадывать число
a = random.randint(1, 100)
# print(a) #раскомитить для проверки случая, когда пользователь угадывает число
b = int(input('Enter digit in range from 1 to 100: '))
if a == b:
    print('You are damn right!')
else:
    print('Sorry, U are not a winner')
