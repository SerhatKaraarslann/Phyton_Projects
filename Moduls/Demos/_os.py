#This module give us a opportunity to take information about our system, make change over file ...
import os

result = dir(os)
print(result)

result = os.name  #nt that means i use windows operation system
print(result)

result = os.getcwd() # information about the pfad the currently file
print(result)

#os.chdir("C:\\") #change directory as C
#os.chdir("..") #to upper directoy like in batch

#os.mkdir("newdirectory") # i created a directory in the currently file
#os.makedirs("newdirectory/newfile") #to create a files under newdirectory

result = os.listdir("D:\\")
print(result)

os.chdir("Moduls")
for file1 in os.listdir():
   if file1.endswith(".py"):
      print(file1)

os.chdir("Demos")
result = os.stat("date.py")  # Hier there are a lot of imformations for example st_size is the height of file in bytes 
print(result)

import datetime

#result = result.st_size/1024  # 2.08984375 KB
#print(result)
#result = datetime.datetime.fromtimestamp(result.st_ctime) #2024-10-13 21:08:07.177516 create time
#print(result)

#result = datetime.datetime.fromtimestamp(result.st_atime) #2024-10-13 21:42:58.742820 last access time
#print(result)

#result = datetime.datetime.fromtimestamp(result.st_mtime) # 2024-10-13 21:42:58.155392 last modifate time
#print(result)
print(os.listdir())
os.chdir("..")
os.chdir("..")
print(os.listdir())
#os.rename("newdirectory","newdirectory2")
#os.removedirs("newdirectory2/newfile")


#path
#we re using this module to change the extention of a file or change name of file 

result = os.path.abspath("_os.py")  # the position of file
result = os.path.dirname("D:\Phyton\_os.py") # path of file
result = os.path.dirname(os.path.abspath("_os.path"))
print(result)

os.chdir("Moduls/Demos")
result = os.path.exists("_os.py") # if the file with this name exist?
print(result)

