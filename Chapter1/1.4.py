# 获取最大最小的N个元素
import heapq
nums= [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # [42, 37, 23] # 获取最大的三个数
print(heapq.nsmallest(1,nums)) # [-4]  # 获取最小数