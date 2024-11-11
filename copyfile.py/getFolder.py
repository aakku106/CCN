import shutil
import os

src = input("Which folder to copy ? ");
ifFolderExist = input("destination folder exist? (y/n) ");


if ifFolderExist.capitalize() == 'Y':
     trg = input("destination folder Name: ");
else:
     r= input("Name the new folder: ");
     os.mkdir(r);
     

files=os.listdir(src)
print("Coping files from ", src)
print(files)

# iterating through all the files
for fname in files:
    # copying the files to the destination folder
    shutil.copy2(os.path.join(src,fname), trg)
    
