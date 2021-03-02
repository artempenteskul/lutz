import sys
import math


print(sys.platform)

print(2 ** 100)
x = 'Spam!'
print(x * 8)

print('hello world')

arr = [1, 2, 3, 'yes']
print(arr)

print(len(str(2 ** 1000000)))
print(math.pi)
print(math.sqrt(87))

m = ['bb', 'aa', 'cc']
m.sort()
print(m)

class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)


bob = Worker('Bob Smith', 5000)
sue = Worker('Sue Jones', 6000)

print(bob.lastName())
print(sue.lastName())
sue.giveRaise(0.12)
print(int(sue.pay))

# Numbers

a = 4
b = 7

print(2 == 2.0)

pi = math.pi
e = math.e

print(math.sin(2 * math.pi / 180))
print(pow(2, 9))
print(min(3, 1, 7, 5), max(9, 44, 2, 56))

s = {1, 2, 'yes', 'no', 8}
print(type(s))

first = 5
second = first
first = 10
print(first)
print(second)

# str str

# part 8

# exception
# arr = [1, 2, 'yes']
# arr.sort()
# print(arr)

# exercises

str = 'green %s and %s' % ('eggs', 'S')
print(str)

x = 'spam'
y = 'eggs'
x, y = y, x
print(x)
print(y)

if x > y:
    x = 1
    y = 2
else:
    x = 2
    y = 1

print()

a = 'spam'
b = 99
c = ['eggs']

print(a, b, c)

yyy = 'killer rabbit'
if yyy == 'roger':
    print('how is jess?')
elif yyy == 'bugs':
    print('whats up, doc?')
else:
    print('Run away!')

# Loops

# while True:
#     print('Type Ctrl-C to stop me!')

T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:
    print(a, b)

keys = ['spam', 'eggs', 'toast']
vals = [1, 4, 6]
d3 = dict(zip(keys, vals))
print(d3)

# generators & iterators