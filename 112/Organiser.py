import os
import shutil

for_dir = "C:/Users/RKCC/Downloads"
to_dir =  "E:/Download Image"

list_of_file = os.listdir(for_dir)
print(list_of_file)

for file_name in list_of_file:
    name , extension = os.path.splitext(file_name)
    print(name)
    print(extension)

    if extension == "":
        continue
    if extension in [ ".pdf" , ".txt" , ".doc" , ".docx"]:
        path1 = for_dir +  '/' + file_name
        path2 = to_dir + '/' + "document_file"
        path3 = to_dir + '/' + "document_file" + '/' + file_name

        if os.path.exists(path2):
            print("Moving" + file_name +"")

            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving" + file_name +"")
            shutil.move(path1,path3)

          


        

