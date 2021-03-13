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

# from __future__ import ...

# classes
class C1:
    def __init__(self, name):
        self.name = name
I1 = C1('Bob')
I2 = C1('Mel')
print(I1.name)

class FirstClass:
    def setdata(self, value):
        self.value = value

    def display(self):
        print(self.value)

first = FirstClass()
second = FirstClass()

first.setdata('King Arthur')
second.setdata('3.14159')

class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' % self.value)

class ThirdClass(SecondClass):
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return ThirdClass(self.value + other)

    def __str__(self):
        return '[ThirdClass: %s]' % self.value

    def mul(self, other):
        self.value *= other

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)

bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=1000)

print(bob.name, bob.pay)
print(sue.name, sue.pay)
# print(bob.name.split()[-1])
# sue.pay *= 1.10
# print(sue.pay)
print(sue)

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mrg', pay)

    def giveRaise(self, percent, bonus=0.10):
        Person.giveRaise(self, percent + bonus)

tom = Manager('Tom Jones',5000)
tom.giveRaise(.10)
print(tom.lastName())
print(tom)

class nextClass:
    def printer(self, text):
        self.message = text
        print(self.message)

# end of classes (class reload)
class Number:
    def __init__(self, start):
        self.data = start

    def __sub__(self, other):
        return Number(self.data - other)

x = Number(5)
y = x - 2
print(y.data)

class Indexer:
    def __getitem__(self, index):
        return index ** 2

x = Indexer()
print(x[9])

class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

# class AddBoth:
#     def __str__(self):
#         return '[Value: %s]' % self.data

class Callee:
    def __call__(self, *args, **kwargs):
        print('Called:', args, kwargs)

c = Callee()
print(c(1, 2, 3))

class Callback:
    def __init__(self, color):
        self.color = color

    def __call__(self):
        print('turn', self.color)

cb1 = Callback('blue')
cb2 = Callback('green')

# B1 = Button(command=cb1)
# B2 = Button(command=cb2)
# cb1()
# cb2()

#templates
class Wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, attrname):
        print('Trace:', attrname)
        return getattr(self.wrapped, attrname)

def factory(aClass, *args, **kwargs):
    return aClass(*args, **kwargs)

# end of 6th part

# exceptions

# def catcher():
#     try:
#         fetcher(x, 4)
#     except IndexError:
#         print('got exception')
#     print('continuing')
#
# catcher()