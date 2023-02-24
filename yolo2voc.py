import os

dataset = 'D:/dataset/seg/VOCdevkit'
trainIds = os.listdir(os.path.join(dataset, 'images', 'train'))
valIds = os.listdir(os.path.join(dataset, 'images', 'val'))
with open('train.txt', 'w') as trainfile:
    for id in trainIds:
        trainfile.write(id.split('.')[0] + '\n')
with open('val.txt', 'w') as valfile:
    for id in valIds:
        valfile.write(id.split('.')[0] + '\n')