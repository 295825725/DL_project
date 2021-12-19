import os
import shutil

PATH = 'E:/Files/NYU/Term 3/project/DL/code/trainimage'
os.chdir(PATH)

for root, dirs, files in os.walk(PATH):
    index = 0
    for f in files:
        path = os.path.join('./', f)
        dst_path = os.path.join('./', f[:-8])
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
        shutil.move(path, dst_path)
        print(index)
        index += 1
