# 怎样在一个序列上保持顺序并消除重复的值
# 1.如果序列上的值是可哈希(hashable)类型，可利用集合和生成器解决
def dedupe(items):
    seen= set()   # 创建一个空集合用set()方法而不是seen={},这是创建空字典
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a= [1, 1, 1, 2, 4, 8, 9]
print(list(dedupe(a)))

# 2.不可哈希类型dict类型,也可用于单个字段、属性或者更大的数据结构消除重复元素
def dedupe1(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
a1= [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe1(a1, key=lambda d: (d['x'],d['y'])))) # [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
print(list(dedupe1(a1, key=lambda d: d['x']))) # [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]