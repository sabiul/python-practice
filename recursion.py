__author__ = 'Rashed'
# def counter(num):
#     print(num)
#     num += 1
#     counter(num)
#
# counter(1)

print((lambda a, b : a + b)(10, 20))

# print('Please input your number:')
# number = int(input())
# temp = number
#
# while number > 1:
#     number -= 1
#     temp = temp*number
#
# if temp == 0:
#     print(1)
# else:
#     print(temp)
# my_list = [2, 3, 4, 5, 6, 7]
#
# def square(x):
#     return x * x
#
# new_list = map(square, my_list)
# print(new_list)
# print(list(new_list))
my_file = open('test.txt', 'r')


content = my_file.read()
print(content)
my_file.close()

my_file = open('test.txt', 'w')
my_file.write('girl sucks.')
my_file.close()

my_file = open('test.txt', 'r')
content = my_file.read()
print(content)
my_file.close()