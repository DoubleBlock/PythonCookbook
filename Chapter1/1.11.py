# 命名切片
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print(cost) # 51325.0

SHARES=slice(20, 23) # 内置的 slice() 函数创建了一个切片对象，可以被用在任何切片允许使用的地方
PRICE= slice(31, 37)
cost1=int(record[SHARES]* float[PRICE])

# 切片对象属性start stop step
s= slice(5, 50, 2)
print(s.start ) # 5
print(s.stop) # 50
print(s.step) # 2