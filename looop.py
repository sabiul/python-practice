__author__ = 'Rashed'
# n = 1
# while n <= 10:
#     print(n)
#     n = n+1

# n = 1
# while n <= 10:
#     print(n)
#     n = n+1
# a = {'name' : 'MD. Maksudur Rahman Khan', 'nickname' : 'Maateen', 'email' : 'maateen@outlook.com', 'phone' : '01711223344'}
#
# print(a)
# print(type(a))
# for item in a:
#     print(item)
#
# range(5, 20, 2)
# l = list(range(5, 20, 2))
# print(l)
# for number in range(1, 11):
#     if number == 5:
#         break
#     print(number)
# for item in range(40,403):
#     print(item)
#
# a = ['onion', 'potato', 'ginger', 'cucumber']
# for item in a:
#     print(item)
# a = [3,45,66,4543,43,'dsdsd']
# for item in a:
#     print(item)
# i = 1
# while i > 0:
#     i += 1
#     print(i)
# ইউজার যেকোন একটা পূর্ণসংখ্যা ইনপুট দেবে। আর ঐ পূর্ণসংখ্যার নামতা আউটপুট হিসাবে দেখাতে হবে।
#
# print('Please, input the number:')
# number = int(input())
# count = 1
#
# while count <= 10:
#     print(number, 'x', count, '=', number*count)
#     count += 1

# print('Please, input the number:')
# number = int(input())
# temp = number
#
# while number > 0:
#     count = temp
#     while count > 0:
#         print('*', end='')
#         count -= 1
#     print()
#     number -= 1



my_list = [i**2 for i in range(20) if i % 2 == 0]
print(my_list)
a_list = ['Maateen', 'Khan', 'Maksudur', 'a', 'b', 'c']
my_set = {i for i in a_list if len(i) > 1}
print(my_set)