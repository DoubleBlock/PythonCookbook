# 使用其他行终止符或分隔符打印输出
print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=',', end='!!\n')
'''
ACME 50 91.5
ACME,50,91.5
ACME,50,91.5!!
'''

# 使用end参数禁止换行
for i in range(5):
    print(i)
'''
0
1
2
3
4
'''

for n in range(5):
    print(n, end=' ')
'''
0 1 2 3 4 
'''