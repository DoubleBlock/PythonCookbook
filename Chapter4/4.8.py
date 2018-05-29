# 跳过可迭代对象的开始部分
# 遍历一个可迭代对象跳过开始的元素
from itertools import dropwhile,islice

with open('4.7.py', encoding='utf-8') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')

# 如果已经知道要跳过元素的个数的话 使用islice()
items=['a', 'b', 1, 2, 3]
for i in islice(items, 2, None):
    print(i)