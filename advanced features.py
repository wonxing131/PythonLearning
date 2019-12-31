from collections import Iterable

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print([L[0], L[1], L[2]])
r = []
n = 3
for i in range(n):
    r.append(L[i])

print(r)
print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[-2:])
print(L[-2:-1])
L = list(range(100))
print(L[:10:2])
print(L[::5])

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for ch in 'ABC':
    print(ch)

print(isinstance('abc', Iterable))  # str是否可迭代

print(isinstance([1, 2, 3], Iterable))  # list是否可迭代

print(isinstance(123, Iterable))  # 整数是否可迭代

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)