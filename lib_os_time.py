import os
import time

print(os.getcwd())
os.chdir('C:\\Users\\vdi-belfer\\Desktop\\folder')
os.mkdir('new_folder')
time.sleep(1)
os.rename('new_folder', 'new_folder2')
time.sleep(1)
os.rmdir('new_folder2')

#znaleźć plik new.txt w danej lokalizacji
os.system('cmd /c "cd C:\\Users\\vdi-belfer\\Desktop\\folder && dir new.txt >> results.txt"')
#&&
#dir new.txt
#  >> result.txt
