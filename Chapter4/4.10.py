# 序列上索引值迭代
# 迭代一个序列的同时跟踪正在被处理元素的索引
from collections import defaultdict


my_list = ['a', 'b', 'c']
for index, value in enumerate(my_list):
    print(index, value)
'''
0 a
1 b
2 c
'''

for idx,val in enumerate(my_list, 1): # 索引从1开始
    print(idx, val)

# 遍历文件时在错误信息中使用行号定位
def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields= line.split()
            try:
                count= int(fields[1])
            except ValueError as e:
                print('Line {}: Parse Error: {}'.format(lineno, e))

# 将一个文件中的单词映射到出现的行号上
word_summary = defaultdict(list)
with open('myfile.txt', 'r') as f:
    lines = f.readlines()
    for idx, line in enumerate(lines):
        # Create a list of words in current line
        words = [w.strip().lower() for w in line.split()]
        for word in words:
            word_summary[word].append(idx)
'''
如果你处理完文件后打印 word summary ， 会发现它是一个字典 (准确来讲是一个
defaultdict )，对于每个单词有一个 key ，每个 key 对应的值是一个由这个单词出现
的行号组成的列表。如果某个单词在一行中出现过两次，那么这个行号也会出现两次，
同时也可以作为文本的一个简单统计。
'''
