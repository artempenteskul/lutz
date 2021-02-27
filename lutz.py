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