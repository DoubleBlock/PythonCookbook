# 排列组合的迭代
# 迭代遍历一个集合中的元素的所有排列或组合
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
items=['a', 'b', 'c']
# for i in permutations(items): # permutations()接受一个集合并产生一个元组序列，每个元组由集合中所有元素的一个可能排列组成
#     print(i)
'''
('a', 'b', 'c')
('a', 'c', 'b')
('b', 'a', 'c')
('b', 'c', 'a')
('c', 'a', 'b')
('c', 'b', 'a')
'''
# for p in permutations(items,2): # 第二个参数指定长度
#     print(p)
'''
('a', 'b')
('a', 'c')
('b', 'a')
('b', 'c')
('c', 'a')
('c', 'b')
'''


# combinations()会忽略元素顺序
for n in combinations(items, 3):
    print(n)
'''
('a', 'b', 'c')
'''

for m in combinations(items, 2):
    print(m)
'''
('a', 'b')
('a', 'c')
('b', 'c')
'''

for o in combinations(items, 1):
    print(o)
'''
('a',)
('b',)
('c',)
'''

# combinations_with_replacement()允许同一个元素被选取多次
for k in combinations_with_replacement(items, 3):
    print(k)
'''
('a', 'a', 'a')
('a', 'a', 'b')
('a', 'a', 'c')
('a', 'b', 'b')
('a', 'b', 'c')
('a', 'c', 'c')
('b', 'b', 'b')
('b', 'b', 'c')
('b', 'c', 'c')
('c', 'c', 'c')
'''

for l in combinations_with_replacement(items, 2):
    print(l)
'''
('a', 'a')
('a', 'b')
('a', 'c')
('b', 'b')
('b', 'c')
('c', 'c')
'''