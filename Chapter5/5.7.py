# 读写压缩文件
# 读写一个gzip或bz2格式的压缩文件
import gzip
import bz2

with gzip.open('somefile.gz', 'rt') as f:
    text= f.read()

with gzip.open('somefile.bz', 'rt') as f:
    text1= f.read()

# compresslevel指定压缩级别
with gzip.open('somefile3.gz', 'wt', compresslevel=5) as f:
    text='hello'
    f.write(text)

'''
gzip.open() 和 bz2.open() 还有一个很少被知道的特性，它们可以作
用在一个已存在并以二进制模式打开的文件上
'''
f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()