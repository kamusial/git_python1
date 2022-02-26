import os
import socket

os.chdir('C:\\Users\\vdi-belfer\\Desktop\\folder')
os.system(f'cmd /c "ipconfig /all > ip.txt"')

with open('C:\\Users\\vdi-belfer\\Desktop\\folder\\ip.txt','r') as ip_file:
    content = ip_file.readlines()
print(content)

for i in content:
    if 'Host Name' in i:
        host_name = i[39:]
    elif 'IPv4 Address' in i:
        ip_address = i[39:-13]

print(host_name)
print(ip_address)

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(hostname)
print(local_ip)
