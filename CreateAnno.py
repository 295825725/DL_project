import os
import pandas as pd

path = './trainimage'
file_list = next(os.walk(path))[1]
# print(file_list)
# file_list.sort()
print(file_list)
file_list.sort(key=lambda x: int(x[5:]))
print(file_list)

anno = []
index = 0
for i in range(int(len(file_list))):
    f = file_list[index]
    if index < 800 or (2400 > index >= 1600):
        anno.append([f, 1])
    else:
        anno.append([f, 0])
    index += 1
PD = pd.DataFrame(data=anno)
print(PD)
PD.to_csv('./train_anno.csv', index=False, header=False)
