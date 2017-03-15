__author__ = 'Rashed'
a = {'name' : 'MD. Maksudur Rahman Khan', 'nickname' : 'Maateen', 'email' : 'maateen@outlook.com', 'phone' : '01711223344'}
print(a)
a['name']
a['name'] = 'Muhammad Maksudur Rahman Khan'
print(a)
a['hometown'] = 'Barisal'
print(a)
b = {'hometown' : 'Barisal', 'fav_poet' : 'Nazrul'}
a.update(b)
del a['phone']

print(a)
p = a.get('name')
print(p)