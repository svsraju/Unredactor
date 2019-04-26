# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 17:38:07 2019

@author: varma
"""

import glob
import io
import os
import pdb
import sys
import numpy as np

import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import pos_tag
from nltk import ne_chunk
from sklearn.feature_extraction import DictVectorizer


def get_entity(text):
    """Prints the entity inside of the text."""
    person_names = []
    for sent in sent_tokenize(text):
        for chunk in ne_chunk(pos_tag(word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                #print(chunk.label(), ' '.join(c[0] for c in chunk.leaves()))
                name = ""
                for c in chunk.leaves():
                    name = name + c[0]
                    name = name + " "
                person_names.append(name[:-1])
    
    word=word_tokenize(text)
    word_count=len(word)
    file=""
    file=text
    for name in person_names:
        file=file.replace(name,len(name)*"█")
        count=file.count("█")
    
    
    feature_list = []
    for name in person_names:
        feature_dict = {}
        space_count = 0
        name_length = len(name)
        for c in name:
            if c ==" ":
                space_count = space_count + 1
          
        feature_dict = {'person_name': name,'name_length' : name_length,'spacing':space_count,'redacted_len': count, 'words_count': word_count}

        feature_list.append(feature_dict)
    
    return feature_list                  
                
                

def doextraction(glob_text):
    all_entities = []
    """Get all the files from the given glob and pass them to the extractor."""
    #for thefile in glob.glob(glob_text):
    for thefile in glob.glob('*.txt'):    
        with io.open(thefile, 'r', encoding='utf-8') as fyl:
            text = fyl.read()
            entites = get_entity(text)
            for entity in entites:
                 all_entities.append(entity)
                
   
    return all_entities     
            
            


doextraction('*.txt')   




######################## Train ################
# creating the training dataset, from the above dictionary

feature_array = []
target_variable = []
full_features = doextraction('*.txt')

for i in full_features:
    target_variable.append(i['person_name'])
    del i['person_name']
    feature_array.append(i)
 
target_variable = np.array(target_variable)  
DV = DictVectorizer(sparse = False)  
    
feature_array = DV.fit_transform(feature_array)    

# Training the the model
# Fitting Kernel SVM to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(feature_array, target_variable)


from sklearn.naive_bayes import GaussianNB
classifier2 = GaussianNB()
classifier2.fit(feature_array, target_variable)


############## prepearing the test data and predicting the names ###########


def get_entity_test(text):
    """Prints the entity inside of the text."""
    person_names = []
    for sent in sent_tokenize(text):
        for chunk in ne_chunk(pos_tag(word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                #print(chunk.label(), ' '.join(c[0] for c in chunk.leaves()))
                name = ""
                for c in chunk.leaves():
                    name = name + c[0]
                    name = name + " "
                person_names.append(name[:-1])
    
    word=word_tokenize(text)
    word_count=len(word)
    file=""
    file=text
    for name in person_names:
        file=file.replace(name,len(name)*"█")
        count=file.count("█")
    
    
    feature_list = []
    for name in person_names:
        feature_dict = {}
        space_count = 0
        name_length = len(name)
        for c in name:
            if c ==" ":
                space_count = space_count + 1
          
        feature_dict = {'person_name': name,'name_length' : name_length,'spacing':space_count,'redacted_len': count, 'words_count': word_count}

        feature_list.append(feature_dict)
    
    return feature_list


def doextraction_test(glob_text):
    all_entities = []
    """Get all the files from the given glob and pass them to the extractor."""
    #for thefile in glob.glob(glob_text):
    for thefile in glob.glob('*.txt'):    
        with io.open(thefile, 'r', encoding='utf-8') as fyl:
            text = fyl.read()
            entites = get_entity_test(text)
            for entity in entites:
                 all_entities.append(entity)
                
   
    return all_entities     
            

feature_array_test = []
actual_names = []
full_features_test = doextraction_test('*.txt')

for i in full_features_test:
    actual_names.append(i['person_name'])
    del i['person_name']
    feature_array_test.append(i)
 
actual_names = np.array(actual_names)  
DV = DictVectorizer(sparse = False)  

    
feature_array_test = DV.fit_transform(feature_array_test)  

predicted_names = classifier.predict(feature_array_test)



         