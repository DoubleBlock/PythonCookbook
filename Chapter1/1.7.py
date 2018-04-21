# 字典排序
# 创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序
from collections import OrderedDict
def order_dic():
    d= OrderedDict()
    d['foo']= 1
    d['bar']= 2
    d['spam'] = 3
    d['grok'] = 4
    for k, v in d:
        print(k, v)
order_dic()