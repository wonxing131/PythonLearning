from functools import reduce


def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)
print(list(r))


def add(x, y):
    return x + y


s = reduce(add, [1, 3, 5, 7, 9])
print(s)


def is_odd(n):
    return n % 2 == 1


r = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(r)


def not_empty(s):
    return s and s.strip()


n = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(n)


print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

