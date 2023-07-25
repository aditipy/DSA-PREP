import os
import shutil
source="/Users/aditi/Desktop/Photos/"
source2="/Users/aditi/Desktop/Video/"
source3="/Users/aditi/Downloads/screenshot/"
target="/Users/aditi/Downloads/"

files=os.listdir(source)
for file in files:
    shutil.move(source+file,target+file)
files2=os.listdir(source2)
for file in files2:
    shutil.move(source2+file,target+file)
files3=os.listdir(source3)
for file in files3:
    shutil.move(source3+file,target+file)