import shutil
import os

folderName = input("Enter the folder name to list its files: ")
filesINFolder=os.listdir(folderName)

for fname in filesINFolder:
    print(fname);
    
    
file_name = input("Enter the file name: ");


if file_name not in filesINFolder:
    print("File not found");
    exit(1);
    

file_path = os.path.join('copyfile',folderName ,file_name)
print("File path: ", file_path);