import os, shutil;
import Phoenix as phx;
def fetchFolder():
      folderName = input("Select folder for versioning: ");
      ifFolderExist = os.path.isdir('../'+folderName);    
      if ifFolderExist :
          shutil.copytree('../'+folderName,phx.returnThrow())
          print("Folder selected: ", folderName, "\n", "Files in the folder:");
          fileName= os.listdir("../"+folderName);
          for i in fileName:
             print(i);
      else:
         print('The folder name you entered  do not exist \n try again');
         fetchFolder();
getCommand=input();
if getCommand == 'ccn catch':
      fetchFolder();  











