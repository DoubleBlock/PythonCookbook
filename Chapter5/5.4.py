# 读写字节数据
# 读写二进制文件比如图片音乐
# 使用模式为 rb 或 wb 的 open() 函数来读取或写入二进制数据




# 从二进制模式的文件中读取或写入文本数据，必须确保要进行解码和编码
# 操作
with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')
with open('somefile1.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))