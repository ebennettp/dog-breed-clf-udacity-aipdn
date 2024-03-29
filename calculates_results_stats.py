#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Ed Bennett
# DATE CREATED: 06/24/23
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs


def calculates_results_stats(results_dic:dict):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog.
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """        
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function

    n_images = len(results_dic)
    n_pet_dog = 0
    n_class_cdog = 0
    n_class_cnotd = 0
    n_match_breed = 0
    n_class_clabel = 0

    incorrect_dog = []
    incorrect_breed = []

    for img_name, img_info in results_dic.items():

        matched_breed = img_info[2]
        is_dog = img_info[3]
        clf_is_dog = img_info[4]

        if is_dog:
            n_pet_dog += 1

            if matched_breed: n_match_breed += 1
            else: incorrect_breed.append(img_name)

            if clf_is_dog: n_class_cdog += 1

        elif clf_is_dog: incorrect_dog.append(img_name)
        else: n_class_cnotd += 1

        if img_info[0] in [sub_label.strip() for sub_label in img_info[1].split(',')]:
            n_class_clabel += 1

    n_pet_notd = n_images - n_pet_dog
    pct_corr_dog = n_class_cdog / n_pet_dog * 100 if n_pet_dog else 100.00
    pct_corr_notdog = n_class_cnotd / n_pet_notd * 100 if n_pet_notd else 100.00
    pct_corr_breed = n_match_breed / n_pet_dog * 100 if n_pet_dog else 100.00
    pct_correct_label = n_class_clabel / n_images * 100 if n_images else 100.00

    results_stats_dic = {
        'n_images': n_images,
        'n_dogs_img': n_pet_dog,
        'n_notdogs_img': n_pet_notd,
        'pct_correct_dogs': pct_corr_dog,
        'pct_correct_breed': pct_corr_breed,
        'pct_correct_notdogs': pct_corr_notdog,
        'pct_correct_label': pct_correct_label,
        'incorrect_dog': incorrect_dog,        
        'incorrect_breed': incorrect_breed
    }

    return results_stats_dic
