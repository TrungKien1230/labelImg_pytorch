# Preprocessing images - Annotation
This ReadMe explains how to use this tool to do annotation

Features include:
* Do annotation and export the file under Darknet and Pytorch format
* Resize the images


### Getting Started
In order to setup the project, please follow the next steps.

#### Copy the tool
Copy the tool from:
```bash
EFR-DL0063-IDEE Data Services - General\40 - Microservices\417 - MS28 Automatic element detection in pictures\4173 - Investigation\R&D_MS28_V1\labelImg

```
#### Prerequisites
* python 3.7

#### Requirements

```bash
pip install -r requirements.txt
```

You can define your label list at:

```bash
.\data\predefined_classes.txt
```



### Run the tool to do annotation

```bash
# At terminal:
python labelImg.py
```
Note: Pay attention at the directory where you save annotated images, make sur that there are at least two exported files .txt for each image, one is _pytorch.txt
If not, please save at least two times while doing annotation for one image

### Convert the dataset from Darknet format to Pytorch format

* Open dir.txt and copy this link to full_path_to_images in creating_train_and_test_txt_files.py.
* Define the ratio of train/test (default is 15% of test, 75% of training)
* Modify the appropriate size of images to do resizing (default is 416x416)

```bash
# At terminal:
python creating_train_and_test_txt_files.py

```


### References

  * LabelImg from Github (https://github.com/tzutalin/labelImg)

### Licenses
Copyright 2020-2021, Umlaut - All Rights Reserved

### Contributors
* Maria Grine [maria.grine@umlaut.com](mailto:maria.grine@umlaut.com)
* Trung-Kien Nguyen [trung-kien.nguyen@umlaut.com](mailto:trung-kien.nguyen@umlaut.com)
