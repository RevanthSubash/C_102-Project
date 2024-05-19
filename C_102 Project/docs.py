import os
import shutil

source="C:/Users/lvsub/Downloads"
destination="C:/Users/lvsub/Desktop"
list_of_files=os.listdir(source)

#print(list_of_files)

for file_name in list_of_files:
    name, extention=os.path.splitext(file_name)
    #print(name)
    #print(extention)
    
    if extention=='':
        continue
    if extention in ['.pdf', '.doc', '.docx', '.log', '.txt', '.msg']:
        path1=source+'/'+file_name
        path2=destination+'/'+"Doc_files"
        path3=destination+'/'+"Doc_files"+'/'+file_name

        if os.path.exists(path2):
            print("moving")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1, path3)