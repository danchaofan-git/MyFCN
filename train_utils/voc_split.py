# ----------------------------------------------------------------------#
#   test.txt和val.txt里面没有内容是正常的。训练不会使用到。
# ----------------------------------------------------------------------#
import os
import random 
random.seed(0)

xmlfilepath  = r'D:\dataset\fcndata\VOCdevkit\VOC2012\SegmentationClass'
saveBasePath = r"D:\dataset\fcndata\VOCdevkit\VOC2012/ImageSets/Segmentation"
if not os.path.exists(saveBasePath):
    os.mkdir(saveBasePath)

# ----------------------------------------------------------------------#
#   想要增加测试集修改trainval_percent
#   train_percent不需要修改
# ----------------------------------------------------------------------#

trainval_percent = 1    # 数据集中训练＋验证集所占用的比例
train_percent    = 0.8      # 训练＋验证集中训练集所占用的比例

temp_xml = os.listdir(xmlfilepath)
total_xml = []
for xml in temp_xml:
    if xml.endswith(".png"):
        total_xml.append(xml)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)
 
print("train and val size", tv)
print("traub suze", tr)
ftrainval = open(os.path.join(saveBasePath, 'trainval.txt'), 'w')
ftest = open(os.path.join(saveBasePath, 'test.txt'), 'w')
ftrain = open(os.path.join(saveBasePath, 'train.txt'), 'w')
fval = open(os.path.join(saveBasePath, 'val.txt'), 'w')
 
for i in list:
    name = total_xml[i][:-4]+'\n'
    if i in trainval:  
        ftrainval.write(name)  
        if i in train:  
            ftrain.write(name)  
        else:  
            fval.write(name)  
    else:  
        ftest.write(name)  
  
ftrainval.close()  
ftrain.close()  
fval.close()  
ftest .close()
