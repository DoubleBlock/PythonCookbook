# 查找两个字典的相同点
# 怎样在两个字典中寻寻找相同点 (比如相同的键、相同的值等等)？
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}
b= {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

# 找出相同的键 &
print(a.keys()& b.keys()) # {'y', 'x'}

# 找不同的键
print(a.keys()- b.keys()) # {'z'}

# 找相同的部分
print(a.items()& b.items()) # {('y', 2)}

# 实现一个新字典
c= {key:a[key] for key in a.keys()- {'z'}}
print(c) # {'x': 1, 'y': 2}