import numpy as np
import os
label_path = 'data/trfg/testing/label.txt'
img_path = 'trfg/testing/'

with open(label_path, encoding='utf8') as file:
    labels = np.loadtxt(file,dtype=object)



for idx, label in enumerate(labels) :
    path = os.path.join(img_path, label[0])
    labels[idx][0] = path
    labels[idx][1] = f'\t{label[1]}'

print(labels)
    
with open('data/gt.txt', "w", encoding="utf-8") as f:
    np.savetxt(f, labels, delimiter='', fmt = '%s')


