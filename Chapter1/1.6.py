# 字典中的键映射多个值
# 值放到另外的容器中 选择使用列表还是集合取决于你的实际需求。如果你想保持元素的插入顺序就应该
# 使用列表，如果想去掉重复元素就使用集合（并且不关心元素的顺序问题）。
from collections import defaultdict
# d = {
#     'a' : [1, 2, 3],
#     'b' : [4, 5]
# }
# e= {
#     'a' : {1, 2, 3},
#     'b' : {4, 5}
# }

# d= defaultdict(list)
# d['a'].append(1)
# d['a'].append(2)
# print(d['a']) # [1, 2]
#
# e=defaultdict(set)
# e['a'].add(1)
# e['a'].add(2)
# e['b'].add(4)
# print(e['a'],e['b']) # {1, 2} {4}
pairs= {'a' : [1, 2, 3],'b' : [4, 5]}
d = defaultdict(list)
for key in pairs:
    d[key].append(value)
    print(d)