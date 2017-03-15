__author__ = 'Rashed'
b = ['onion', 'potato', 'ginger', 'cucumber', 1, 3.1416]
print(b)
print(type(b[4]))
b.append('new')
print(b)
b.insert(1, 'python')
print(b)
b.extend(['a', 'b', 'c'])

print(b)
b = b + ['a', 'b', 'c']
print(b)
b.pop()
print(b)
b.pop()
print(b)
c = ['potato', 'a', 'b', 'potato', 'potato']
print(c.count('potato'))
o = b.reverse()
print(o)

k=['rice', 'python', 'potato', 343, 'cucumber', 'finger', 23486.4678]
o = k.reverse()
print(o)

L = [0,10,20,40]

L.reverse()
print(L)
L[::-1]
print(L)
L.sort()
print(L)