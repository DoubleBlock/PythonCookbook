# 通过某个字段将记录分组
from operator import itemgetter
from itertools import groupby

rows= [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
rows.sort(key=itemgetter('date')) # 必须先给数据排序，否则接下来使用groupby得不到想要的结果
print(rows)
for date, item in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in item:
        print(' ', i)