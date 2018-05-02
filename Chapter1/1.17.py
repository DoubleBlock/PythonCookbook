# 从字典中提取子集
# 字典推导
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
p={key:value for key, value in prices.items() if value > 200}
p1= dict((key, value) for key, value in prices.items() if value > 200)
print(p, p1)