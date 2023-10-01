# # Завдання 1
# #
# # У списку цілих, заповненому випадковими числами обчислити:
# #
# # ■ Суму негативних чисел;
# #
# # ■ Суму парних чисел;
# #
# # ■ Суму непарних чисел;
# #
# # ■ Добуток елементів з кратними індексами 3;
# #
# # ■ Добуток елементів між мінімальним та максимальним елементом;
# #
# # ■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.
#
# try:
#  import random
#
#  numbers = [random.randint(-100,100)for _ in range(20)]
#  print(f"Numbers : {numbers}")
#
# # ■ Суму негативних чисел;
#
#  negative = 0
#  for i in numbers:
#   if i < 0 :
#    negative += i
#  print(f"Sum of negative numbers : {negative}")
#
# # ■ Суму парних чисел;
#
#  paired = 0
#
#  for i in numbers:
#   if i % 2 == 0:
#    paired += i
#  print(f"Sum of paired numbers : {paired}")
#
# # ■ Суму непарних чисел;
#
#  unpaired  = 0
#
#  for i in numbers:
#   if i % 2 != 0:
#    unpaired  += i
#  print(f"Sum of unpaired numbers : {unpaired}")
#
# # ■ Добуток елементів з кратними індексами 3;
#
#  multiples_3  = 1
#
#  for i in numbers:
#   if i % 3 == 0:
#    multiples_3 *= i
#  print(f"Product of elements with multiple indices 3 : {multiples_3}")
#
# # ■ Добуток елементів між мінімальним та максимальним елементом;
#
#  max = max(numbers)
#  min = min(numbers)
#  multiplication = 1
#  for i in numbers:
#   if i > min and i < max:
#    multiplication *= i
#  print(f"The product of elements between the minimum and maximum element "
#       f"\n: {multiplication}")
#
# # ■ Суму елементів,
# # що знаходяться між першим та останнім позитивними елементами.
#
#  nums_sum = 0
#  first = last = 0
#  for i in range(len(numbers)):
#      if numbers[i] > 0:
#          first = i
#          break
#
#  for i in range(len(numbers) - 1, -1, -1):
#      if numbers[i] > 0:
#          last = i
#          break
#  print(f"Index of the first positive element : {first}")
#  print(f"Index of the last positive element : {last}")
#
#  result = 0
#
#  for i in range(first + 1, last):
#   result += numbers[i]
#
#  print(f"The sum of elements,"
#       f"located between the first and "
#        f"last positive elements : {result}")
# except ValueError as error:
#     print(error)

# # Завдання 2
# #
# # Є список цілих, заповнений випадковими числами.
# #
# # На підставі даних цього масиву потрібно:
# #
# # ■ Створити список цілих, що містить лише парні числа з першого списку;
# #
# # ■ Створити список цілих, що містить лише непарні числа з першого списку;
# #
# # ■ Створити список цілих, що містить лише негативні числа з першого списку;
# #
# # ■ Створити список цілих, що містить лише позитивні числа з першого списку.
#
# try:
#  import random
#
#  numbers = [random.randint(-100,100)for _ in range(20)]
#  print(f"Numbers : {numbers}")
#
# # ■ Створити список цілих,
# # що містить лише парні числа з першого списку
#
#  paired = [i for i in numbers if i % 2 == 0]
#  print(f"Paired numbers : {paired}")
#
# # ■ Створити список цілих,
# # що містить лише непарні числа з першого списку;
#
#  not_paired = [i for i in numbers if i % 2 != 0]
#  print(f"Not paired numbers : {not_paired}")
#
# # ■ Створити список цілих,
# # що містить лише негативні числа з першого списку;
#
#  negative = [i for i in numbers if i < 0 ]
#  print(f"Negative numbers : {negative}")
#

# # ■ Створити список цілих,
# # що містить лише позитивні числа з першого списку.
#
#  positive = [i for i in numbers if i > 0 ]
#  print(f"Positive numbers : {positive}")
#
# except ValueError as error:
#     print(error)
