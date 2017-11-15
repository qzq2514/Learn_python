#StringIO只能读写字符串str,读取二进制数据，就需要使用BytesIO
from io import BytesIO
f=BytesIO()
n=f.write("中文祁忠琪".encode('utf-8'))
#write()函数返回字节数
print(n)
#getvalue()返回字节数据，以十六进制形式
#注意，写入的不是str，而是经过UTF-8编码的bytes
print(f.getvalue())
#b'\xe4\xb8\xad\xe6\x96\x87\xe7\xa5\x81\xe5\xbf\xa0\xe7\x90\xaa'


r=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87\xe7\xa5\x81\xe5\xbf\xa0\xe7\x90\xaa')
buf=r.read()
print(buf)
print(buf.decode("utf-8"))#解码得到字符串