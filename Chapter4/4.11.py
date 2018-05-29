from itertools import zip_longest
# 同时迭代多个序列
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x, y)
'''
1 101
5 78
4 37
2 15
10 62
7 99
'''

#zip(a, b) 会生成一个可返回元组 (x, y) 的迭代器，其中 x 来自 a， y 来自 b。一
#旦其中某个序列到底结尾，迭代宣告结束。因此迭代长度跟参数中最短序列长度一致。

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a, b):
     print(i)
'''
(1, 'w')
(2, 'x')
(3, 'y')
'''

# zip_longest()自适应最长序列，无第三个参数自动填充，指定参数按指定参数填充
for m in zip_longest(a, b):
    print(m)
'''
(1, 'w')
(2, 'x')
(3, 'y')
(None, 'z')
'''

for n in zip_longest(a, b, fillvalue=4):
    print(n)
'''
(1, 'w')
(2, 'x')
(3, 'y')
(4, 'z')
'''

headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
s= dict(zip(headers, values))
print(s)