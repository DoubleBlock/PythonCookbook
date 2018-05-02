# 通过某个关键字排序字典列表
from operator import itemgetter
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
rows_by_fname= sorted(rows, key=itemgetter('fname')) # 按fname排序
rows_by_uid = sorted(rows, key=itemgetter('uid')) # 按uid排序
print(rows_by_fname)
print(rows_by_uid)

# itemgetter() 函数也支持多个 keys
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print(rows_by_lfname)

# itemgetter() 有时候也可以用 lambda 表达式代替 但性能不如itemgetter()
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname']))

# min() max()