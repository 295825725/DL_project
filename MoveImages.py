import os
import shutil

rootdir = "."

list = os.listdir(rootdir)

for i in range(0, len(list)):
    path = os.path.join(rootdir, list[i])
    if os.path.isdir(path) and list[i][0:13] == "trainimageOut":
        print(path)
        j = 0
        for item in os.listdir(path):
            dirname = os.path.join(".", list[i])
            full_path = os.path.join(dirname, item)
            des_path = "./trainimage/" + item
            print(full_path)
            print(des_path)
            shutil.move(full_path, des_path)
            print(j)
            j += 1
