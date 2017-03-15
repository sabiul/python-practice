__author__ = 'Rashed'

"""
a = int(input())
b = int (input())
if a == 5:
    print('a is equal to 5.')
elif a < 5:
    print('a is less than 5.')
elif a > 5 and a < 10:
    print('a is inbetween 5 and 10.')
else:
    print('a is greater than 10.') """

a = int(input())
if a < 10:
    if (a % 2) == 0:
        print('less, yes')
    else:
        print('less, no')
else:
    if (a % 3) == 0:
        print('greater, yes')
    else:
        print('greater, no')