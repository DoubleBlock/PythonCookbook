# 合并多个映射或字典
# 有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某些
# 操作，比如查找值或者检查某些键是否存在。
from collections import ChainMap
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
c= ChainMap(a, b)
print(c['z']) # 3 如果出现重复键， 那么第一次出现的映射值会被返回