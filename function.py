import math

print(abs(100))
print(abs(-20))
print(abs(12.34))
print(max(1, 2))
print(max(2, 3, 1, -5))
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-99))


def nop():
    pass


age = 1
if age >= 18:
    pass


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


my_abs(-1)


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5, 2))


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2))

nums = [1, 2, 3]
print(calc(*nums))


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)
person('Bob', 35, city='Beijing')


def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')

# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。


def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)


print(fact(5))