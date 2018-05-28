# 反向迭代
# 反向迭代一个序列
# 使用内置reverse()函数
a= [1, 2, 3, 4]
for x in reversed(a):
    print(x)

# 此方法仅仅当对象的大小确定或实现了__reverse__()特殊方法，如果两者都不符合需要将对象转换成列表
f = open('1.txt')
for line in reversed(list(f)):
    print(line, end='')
# 如果可迭代对象元素很多的话list()方法将消耗大量内存

# 通过在自定义类上实现__reverse__()方法来实现反向迭代
class Countdown():
    def __init__(self, start):
        self.start= start

    def __iter__(self):
        n= self.start
        while n> 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

for rr in reversed(Countdown(30)):
    print(rr)
for rr in Countdown(30):
    print(rr)