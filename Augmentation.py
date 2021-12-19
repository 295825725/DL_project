import os
import pandas as pd
from torchvision.io import read_image
import torchvision.transforms as TF
from torchvision.io import write_jpeg

annotations_file = './train_anno.csv'
img_dir = 'E:/Files/NYU/Term 3/project/DL/code/trainimage'

img_labels = pd.read_csv(annotations_file, header=None)
Transform = TF.RandomHorizontalFlip(p=1)
count = 0

for idx in range(len(img_labels)):
    Dirname = img_labels.iloc[idx, 0][0:5] + str(idx + 1600)
    dst_path = os.path.join(img_dir, Dirname)
    os.mkdir(dst_path)
    for i in range(150):
        img_path = os.path.join(img_dir, img_labels.iloc[idx, 0],
                                img_labels.iloc[idx, 0] + '_' + str(i).zfill(3) + '.jpg')
        img = read_image(img_path)
        image = Transform(img)
        file = os.path.join(dst_path, Dirname + '_' + str(i).zfill(3) + '.jpg')
        write_jpeg(image, file)
        count += 1
        print(count)
