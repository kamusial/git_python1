import os
import datetime
import time

now = datetime.datetime.now()
timer = now.strftime('%H_%M_%S')
path = 'C:\\Users\\vdi-belfer\\Desktop\\folder\\' + timer + 'tmp.txt'

ts1 = time.time()
os.system(f'cmd /c "cd C:\ && tracert 8.8.8.8 > {path}"')
ts2 = time.time()

print(f'Komenda Tracert trwała {round(ts2-ts1)} sekund')


