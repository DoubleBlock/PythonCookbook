# 文件不存在才能写入
# 向一个文件中写入数据但这个文件不能存在
with open('somefile', 'xt') as f:
    f.write('hello\n')

# 如果文件是二进制的用xb代替xt