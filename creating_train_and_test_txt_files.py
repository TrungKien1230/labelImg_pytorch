"""
    This function allows to split dataset into 2 files: test and train from the darknet dataset
    Resize the pictures
"""


import os
from shutil import copyfile
import cv2

# Copy this path from dir.txt
full_path_to_images = r'C:\Users\nguy\Documents\TrungKien\Project\IDEE\Gits\labelImg\data\data_test_1_2'

# Define the ratio of train/test
percent_test = 0.15

# Resize the pictures

resized_height = 416
resized_width = 416


# Set this path as current directory
os.chdir(full_path_to_images)

# Take the list of labels
l = open("classes.txt", "r")
labels = l.read().split('\n')[:-1]

# Create file
try:
    os.mkdir('./train')
except:
    pass

try:
    os.mkdir('./test')
except:
    pass

try:
    os.mkdir('./resized_picture')
except:
    pass
p = list()

for current_dir, dirs, files in os.walk('.'):
    # Going through all files
    for f in files:

        # Checking if filename ends with '.jpeg'

        if f.endswith('.jpg'):
            with open(f.split('.')[0]+'_pytorch'+'.txt', 'r+') as draft_txt:

                # Going through all elements of the list
                cont = draft_txt.read().split('\n')[:-1]
                cont = [i.split(' ') for i in cont]
                anno = os.path.join(full_path_to_images, f) + ' '
                img = cv2.imread(os.path.join(full_path_to_images, f), cv2.IMREAD_UNCHANGED)
                img_shape = img.shape
                resized_img = cv2.resize(img, (resized_width, resized_height), interpolation=cv2.INTER_AREA)
                cv2.imwrite(os.path.join("./resized_picture", f), resized_img)

                for idx, val in enumerate(cont):
                    if len(val) > 5:
                        label = " ".join(val[:-4])
                        idx_label = str(labels.index(label))
                        val = val[-4:]
                        val.append(idx_label)
                    else:
                        label = val[0]
                        idx_label = str(labels.index(label))
                        val = val[-4:]
                        val.append(idx_label)

                    if idx != len(cont)-1:
                        anno = anno + str(int(int(val[0]) * resized_width / img_shape[1])) + ',' + str(
                            int(int(val[1]) * resized_height / img_shape[0])) + ',' + str(int(int(
                            val[2]) * resized_width / img_shape[1])) + ',' + str(
                            int(int(val[3]) * resized_height / img_shape[0])) + ',' + val[4] + ' '
                    else:
                        anno = anno + str(int(int(val[0]) * resized_width / img_shape[1])) + ',' + str(
                            int(int(val[1]) * resized_height / img_shape[0])) + ',' + str(int(int(
                            val[2]) * resized_width / img_shape[1])) + ',' + str(
                            int(int(val[3]) * resized_height / img_shape[0])) + ',' + val[4] + '\n'
                p.append(anno)
    break

#Test data
p_test = p[:int(len(p) * percent_test)]
print('p_test: ',len(p_test))
# Train data
p_train = p[int(len(p) * percent_test):]
print('p_train: ',len(p_train))
# Creating file train.txt and writing 85% of lines in it


with open('./train/_annotations.txt', 'w') as train_txt:
    for e in p_train:
        train_txt.write(os.path.join(full_path_to_images, "train",os.path.basename(e)))
        src = os.path.join(full_path_to_images,"resized_picture", os.path.basename(e).split(' ')[0])
        dst = os.path.join(full_path_to_images, "train", os.path.basename(e).split(' ')[0])
        copyfile(src, dst)

with open('./train/_classes.txt', 'w') as class_txt:
    for e in labels:
        class_txt.write(e + '\n')


with open('./test/_annotations.txt', 'w') as test_txt:
    for e in p_test:
        test_txt.write(os.path.join(full_path_to_images, "test", os.path.basename(e)))
        src = os.path.join(full_path_to_images, "resized_picture", os.path.basename(e).split(' ')[0])
        dst = os.path.join(full_path_to_images, "test", os.path.basename(e).split(' ')[0])
        copyfile(src, dst)

with open('./test/_classes.txt', 'w') as class_txt:
    for e in labels:
        class_txt.write(e + '\n')