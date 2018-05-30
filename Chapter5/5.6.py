# 字符串的I/O操作
# 使用操作类文件对象的方法操作文本或二进制字符串
from io import StringIO, BytesIO

s= StringIO()
s.write('hello\n')


m= BytesIO()
m.write(b'hello')