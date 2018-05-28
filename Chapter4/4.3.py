# 实现新的迭代模式，使用一个生成器函数来定义它
def frange(start, stop, increment ):
    x= start
    while x< stop:
        yield x
        x+= increment

for m in frange(0, 4, 0.5):
    print(m)
'''
0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
'''
list(frange(0,1, 0.125))
'''
[0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875]
'''