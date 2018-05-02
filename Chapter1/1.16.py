# 过滤序列元素

# 使用列表推导(占用大量内存)
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])

# 使用生成器表达式迭代
mylist1 = [1, 4, -5, 10, -7, 2, 3, -1]
pos= (n for n in mylist1 if n > 0)
for i in pos:
    print(i)

