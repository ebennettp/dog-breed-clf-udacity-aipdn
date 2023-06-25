# Udacity AIPND - Dog Breed Classifier

## Overview

Classifies pet images using a pretrained CNN model, compares these
classifications to the true identity of the pets in the images, and
summarizes how well the CNN performed on the image classification task.
Note that the true identity of the pet (or object) in the image is 
indicated by the filename of the image. Therefore, your program must
first extract the pet image label from the filename before
classifying the images using the pretrained CNN model. With this 
program we will be comparing the performance of 3 different CNN model
architectures to determine which provides the 'best' classification.


## Note

These models (ResNet, AlexNet, or VGG) are pre-trained and provided by
Udacity's staff members. The purpose of this project is to build the general
functionality of the script to use the different CNN models and compare the
results regarding performance and accuracy.


## How to

### Run the scrpit

To run the program with its default values you can simply execute the shell
script `run_models_batch.sh`, which will use the images insede the `pet_images`
foler and run all 3 models. The output of each model will be redirected into
different local files defined in the this shell script.

The starting point to run the program is `classify_images.py`, which takes
3 optional parameters:
- --dir : str = Path to folder that contains the pet images. Default="pet_images",
- --arch : str = The CNN model architecture to use. Possible values are: resnet, alexnet, or vgg. Default="vgg"
- --dogfile : str = Path to folder that contains the list of valid dog names. Default="dognames.txt",
