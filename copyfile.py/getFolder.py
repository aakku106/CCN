# importing required packages
import shutil
import os

src = 'test'
trg = 'destination'

files=os.listdir(src)

# iterating through all the files
for fname in files:
    # copying the files to the destination folder
    shutil.copy2(os.path.join(src,fname), trg)
    
