from itertools import chain
# 不统集合上元素的迭代
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)