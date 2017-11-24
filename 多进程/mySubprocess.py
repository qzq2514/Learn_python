import subprocess
#subprocess模块可以让我们方便地启动一个进程

#DNS记录的生存时间还可以指定使用哪个DNS服务器进行解释
'''print("$ nslookup www.python.org")
r=subprocess.call(['nslookup','www.python.org'])
print("返回码:",r)'''

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))     #某个字符无法解析
print('Exit code:', p.returncode)