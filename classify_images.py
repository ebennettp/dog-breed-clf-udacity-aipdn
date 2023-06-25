#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Ed Bennett
# DATE CREATED: 06/24/23
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 


def classify_images(images_dir:list, results_dic:dict, model:str):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function.

    Parameters: 
        images_dir - The (full) path to the folder of images that are to be
                     classified by the classifier function (string)
        results_dic - Results Dictionary with 'key' as image filename and 'value'
                      as a List. Where the list will contain the following items: 
                    index 0 = pet image label (string)
                  --- where index 1 & index 2 are added by this function ---
                    NEW - index 1 = classifier label (string)
                    NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                      and classifer labels and 0 = no match between labels
        model - Indicates which CNN model architecture will be used by the 
                classifier function to classify the pet images,
                values must be either: resnet alexnet vgg (string)
    Returns:
        None - results_dic is mutable data type so no return needed.
    """
    for image_name, image_label in results_dic.items():

        img_path = f"{images_dir}/{image_name}"
        prediction = classifier(img_path, model)

        pred_labels = prediction.strip().lower()

        # sepparate into possible names for a same label
        pred_labels_arr = [sub_label.strip() for sub_label in pred_labels.split(',')]

        image_label.append(pred_labels)

        # compare true label to the prediction's different label names
        image_label.append(1 if image_label[0] in pred_labels_arr else 0)
