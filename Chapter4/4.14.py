# 展开嵌套的序列
# 包含yield from语句的递归生成器
from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items= [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)

