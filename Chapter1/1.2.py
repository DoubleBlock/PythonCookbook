# 从可迭代对象中解压N个元素
# 解决方案：星号表达式
# 去掉第一个和最后一个成绩
def drop_first_last(grades):
    first, *middle, last= grades
    print(*middle)

s=[1, 2, 3, 4, 5]
drop_first_last(s) # 2 3 4

#将前七个月的平均值与当月值作对比
*trailing_qtrs, current_qtr = [10,5,7,8,4,6,8,9]
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
print(trailing_avg, current_qtr) # 6.857142857142857 9


records=[
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]
def get_foo(x, y):
    print('foo', x, y)

def get_bar(s):
    print('bar', s)

for tags, *args in records:
    if tags== 'foo':
        get_foo(*args)
    elif tags== 'bar':
        get_bar(*args)
# foo 1 2
# bar hello
# foo 3 4


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname, homedir, sh) # nobody   /var/empty   /usr/bin/false


