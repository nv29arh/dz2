# Задача 1
# Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.

# for i in range(1,6):
#     print(i, 0)

# Задача 2
# Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5
#
# sum = 0
# for i in range(1,11):
#     number = int(input('Введите число '))
#     if number == 5:
#         sum += 1
# print('Количество введенных пользователем цифр 5 = ', sum)


# Задача 3
# # Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран
# sum = 0
# for i in range(1,101):
#     sum +=i
# print(sum)

# Задача 4
# Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
# multiply = 1
# for i in range(1,11):
#     multiply *= i
# print(multiply)


# Задача 5
# Вывести цифры числа на каждой строчке.

# number = int(input('Введите число'))
# while number>0:
#     print(number%10)
#     number = number//10

# Задача 6
# Найти сумму цифр числа.

# number = int(input('Input a number '))
# sum = 0
# while number>0:
#     sum +=number%10
#     number = number//10
# print('Сумма всех цифр числа =', sum)

# Задача 7
# Найти произведение цифр числа.

# number = int(input('Input a number '))
# multiply = 1
# if number == 0:
#     print('Введите число отличное от 0')
# else:
#     while number > 0:
#         multiply *= number%10
#         number = number//10
#     print(multiply)

# Задача 8
# Дать ответ на вопрос: есть ли среди цифр числа 5?

# number = int(input('Input a number'))
# while number>0:
#     if number%10 == 5:
#         print('Yes')
#         break
#     number = number//10
# else: print('No')



# Задача 9
# Найти максимальную цифру в числе

# number = int(input('Input a number'))
# maximum = 0
# while number > 0:
#     if number%10 > maximum:
#         maximum = number%10
#     number = number//10
# print(maximum)

# Задача 10
# Найти количество цифр 5 в числе
#
# number = int(input('Input a number'))
# sum = 0
# while number > 0:
#     if number%10 == 5:
#         sum +=1
#     number = number//10
# print(sum)