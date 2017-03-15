__author__ = 'Rashed'
c = "Bangladesh is my 'motherland', I love her very much."
print(c)
c = "Bangladesh is my \"motherland\", I love her very much."
print(c)
c = "Bangladesh is my 'motherland', I love her very much."
print(c)

a = 'bangla'
print(a[0])

a[1]
a[1:4]
a[:1]
a[:3]
a[2:]
a[4:]
a[-1]
a[-2]
print('My favorite language is:', a)
print('My favorite language is: %s' %a)
number = 436.15757823658945
print('%.2f' % number)
x = 'dhaka'
print(x)
y = 'barisal'


z= 'sylhet'
v=x + '-' + y + '-' + z
print(v)


sentence = 'How can a clam cram in a clean cream can?'
print(sentence.split(' '))
sentence.count('c')
print(sentence.count('c', 5, 9))
print(sentence.count('c', 5,15 ))