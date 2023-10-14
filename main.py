# №1
# def is_prome(a):
#
#     if a == 1:
#         return False
#
#     if a == 2 or a % 2 != 0:
#         for i in range(3, int(a ** 0.5), 2):
#             if a % i == 0:
#                 return False
#         return True
#     return False
#
# b = int(input('Введите число: '))
# print(is_prome(b))

# №2
# l = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]
#
# for i in range(len(l)):
#     for j in range(i + 1, len(l)):
#
#         if l[i] > l[j]:
#            l[i], l[j] = l[j], l[i]
#
# print l

# №3
# def max_green_apple(apple):
#     apple_max = 0
#
#     for i in range(0, len(apple)):
#         if apple[i] > apple_max:
#             apple_max = apple[i]
#
#     return 'Наибольшее число: ' + str(apple_max)
#
#
# apple = []
# apple_size = int(input('Введите количество элементов массива: '))
#
# for i in range(0, apple_size):
#     apple.append(int(input('Введите число для элемента массива ' + str(i)+': ')))
#
# print(max_green_apple(apple))

# № 4
# fib1 = 1
# fib2 = 1
#
# n = input("Номер элемента ряда Фибоначчи: ")
# n = int(n)
#
# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
# print("Значение этого элемента:", fib2)

# №5
# def repeat_words(array_):
#     repeat_words = []
#
#     for i in range(0, array_size):
#         repeat_words.append(0)
#
#     for i in range(0, len(array_)):
#         for j in range(0, len(array_)):
#             if array_[i] == array_[j]:
#                 repeat_words[i] += 1
#
#     index_repeat_word = -1
#
#     for i in range(0, len(array_)):
#         if repeat_words[i] > index_repeat_word:
#             index_repeat_word = i
#
#     if index_repeat_word == -1:
#         return 'Строки не повторяются'
#     else:
#         return index_repeat_word
#
# array = []
# array_size = int(input('Введите количество элементов массива: '))
#
# for i in range(0, array_size):
#     array.append(input('Введите строку для элемента массива ' + str(i)+': '))
#
# print(array[repeat_words(array)])