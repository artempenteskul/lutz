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

# documentation
print(dir([]))

# for i in range(50):
#     print('hello %d' % i)

# functions

def times(q, w):
    return q * w
print(times(5, 9))

def intersect(seq1, seq2):
    res = []
    for smth in seq1:
        if smth in seq2:
            res.append(smth)
    return res
s1 = 'SPAM'
s2 = 'SCAM'
print(intersect(s1, s2))

m, n = 4, 9
def all_global():
    global k
    k = m + n
    print(k)
all_global()

# arguments
def func(spam, eggs, toast=0, ham=0):
    print(spam, eggs, toast, ham)
func(1, 2)
func(1, ham=1, eggs=0)

def f(a, *args, **kwargs):
    print(a, args, kwargs)
f(1, (1, 2), x=1, y=2)

# поиск минимального числа
def min1(*args):
    res = args[0]
    for arg in args:
        if arg < res:
            res = arg
    return res
print(min1(1, 23, 89, 81, -88,))

def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
        return first
print(min2('bb', 'aa'))

def min3(*args):
    tpm = list(args)
    tpm.sort()
    return tpm[0]
print(min3([1, 1], [1, 3], [2, 5]))

# extra functions
l = [1, 3, 4, 4, 5, 5, 9]
sum = 0
while l:
    sum += l[0]
    l = l[1:]
print(sum)

# lambda
def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)
    return action
act = knights()
print(act('Robin'))

counters =  [1, 2, 3, 7, 8, 89, 99]
print(list(map((lambda x: x + 3), counters)))

# list(range(-5, 5))
# print(filter((lambda x: x > 0), range(-5, 5)))

# generators & iterators
def gensquares(N):
    for i in range(N):
        yield i ** 2
for i in gensquares(5):
    print(i, end= ' : ')
print('its working')

# modules

import sys
print(sys.path)