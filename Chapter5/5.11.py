# 文件路径名操作
from os import path


file_path= '/Users/beazley/Data/data.csv'
s= path.basename(file_path)
m= path.dirname(file_path)
print(s, m)


