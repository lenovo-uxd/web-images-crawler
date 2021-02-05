import os, zipfile
import shutil

dir_name = 'C:\\Users\\jinyc\\Desktop\\images\\images'
extension = ".zip"

os.chdir(dir_name)

for item in os.listdir(dir_name):
    if item.endswith(extension):
        file_name = os.path.abspath(item)
        zip_ref = zipfile.ZipFile(file_name)
        zip_ref.extractall()
        pic_nameList = file_name.split("\\")
        pic_name = pic_nameList[len(pic_nameList)-1].split(".")[0]
        print(pic_name)

        for filename in os.listdir(r''+dir_name+"\\"+pic_name):
            if filename.endswith("png"):
                shutil.move("./"+pic_name+"/"+filename, "./"+filename)
                zip_ref.close()
        #os.remove(file_name)