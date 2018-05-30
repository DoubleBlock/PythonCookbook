# 打印输出至文件中
# 在print函数中指定file关键字
with open('test.txt', 'wt') as f: # 文件必须以文本模式打开
    print('hello world', file=f)
