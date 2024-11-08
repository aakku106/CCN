
import shutil
import os

filesINFolder=os.listdir('test')

for fname in filesINFolder:
    print(fname)


file_name = input("Enter the file name: ");

if file_name != filesINFolder:
    print("File not found")
    exit(1)

file_path = os.path.join('copyfile.py','test' ,file_name)
print("File path: ", file_path)