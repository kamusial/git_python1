import os
import time

print(os.getcwd())
os.chdir('C:\\Users\\vdi-belfer\\Desktop\\folder')
os.mkdir('new_folder')
time.sleep(3)
os.rename('new_folder', 'new_folder2')
time.sleep(3)
os.rmdir('new_folder2')
