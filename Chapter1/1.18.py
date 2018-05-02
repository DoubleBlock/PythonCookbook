# 映射名称到序列元素
from collections import namedtuple
Subscriber= namedtuple('Subscriber', ['addr', 'joined'])
sub= Subscriber('chentangyao@gmail.com', '2018.05.02')
print(sub.addr) # chentangyao@gmail.com