import numpy as np
import os
label_path = 'data/trfg/testing/label.txt'
img_path = 'trfg/testing/'

with open(label_path, encoding='utf8') as file:
    labels = np.loadtxt(file,dtype=object)

# print(labels)

for label in labels:
    path = os.path.join(img_path, label[0])
    label[0] = path


with open('data/gt.txt', "w", encoding="utf-8") as f:
    np.savetxt(f, labels, delimiter=' ', fmt = '%s')


