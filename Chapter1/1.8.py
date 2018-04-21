# 字典的运算
# 求最小值、最大值、排序
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
min_price= min(zip(prices.values(),prices.keys())) # zip()将键值的殊勋反转
print(min_price) # (10.75, 'FB')
max_price= max(zip(prices.values(),prices.keys()))
print(max_price) # (612.78, 'AAPL')

# 价格从小到大排序
prices_sorted= sorted(zip(prices.values(),prices.keys()))
print(prices_sorted)
# [(10.75, 'FB'), (37.2, 'HPQ'),(45.23, 'ACME'), (205.55, 'IBM'),(612.78, 'AAPL')]

min(prices,key=lambda k: prices[k]) # 'FB'
max(prices,key=lambda k: prices[k]) # 'AAPL'

# 多个键拥有相同的值是 键会决定返回结果
prices1= {'AAA': 45.23, 'BBB': '45.23'}
min_price1= min(zip(prices1.values(),prices1.keys())) # zip()将键值的殊勋反转
print(min_price1) # (45.23, 'AAA')
max_price1= max(zip(prices1.values(),prices1.keys()))
print(max_price1) # (45.23, 'BBB')