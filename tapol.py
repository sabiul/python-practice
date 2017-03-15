__author__ = 'Rashed'
A = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

{'apple', 'orange', 'banana', 'pear'}
A.add('pineapple')
A.update({'berry', 'grape'})
print(A)
n = {1, 2, 3, 4, 5}
B = {2, 3, 4, 5, 6, 7}
p = n.intersection(B)
print(p)
