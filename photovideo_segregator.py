import os
import shutil
path="/Users/aditi/Downloads/"
dest_vid="/Users/aditi/Desktop/Video/"
dest_img="/Users/aditi/Desktop/Photos/"
file_name=os.listdir(path)


for file in file_name:
    if '.png' in file:
        shutil.move(path+file,dest_img+file)

    elif '.mp4' in file or '.mov' in file:
        shutil.move(path+file,dest_vid+file)

file_name2=os.listdir(dest_img)
for file in file_name2:
    if 'Screenshot' in file:
            shutil.move(dest_img+file,dest_img+'screenshot/'+file)


