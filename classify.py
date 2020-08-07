# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 23:47:34 2020

@author: pulkit
"""
import os
from collections import Counter
import math

def classify(model, filepath):
    dict = {}
    c1 = 0
    c2 = 0
    dict.update({'log p(y=2020|x)': 0})
    dict.update({'log p(y=2016|x)': 0})
    dict.update({'predicted y': 0})
    vocab = model['vocabulary']
    bwords = create_bow(vocab, filepath)
    for i in bwords:
        if i in model['log p(w|y=2016)']:
            c1 = c1 + bwords[i] * model['log p(w|y=2016)'][i]
        else:
            c1 = c1 + bwords[i] * model['log p(w|y=2016)'][None]
    for i in bwords:
        if i in model['log p(w|y=2020)']:
            c2 = c2 + bwords[i] * model['log p(w|y=2020)'][i]
        else:
            c2 = c2 + bwords[i] * model['log p(w|y=2020)'][None]
    c1 = c1 + model['log prior']['2016']
    c2 = c2 + model['log prior']['2020']
    dict.update({'log p(y=2020|x)': c2})
    dict.update({'log p(y=2016|x)': c1})
    if (c1 >= c2):
        res = '2016'
    else:
        res = '2020'
    dict.update({'predicted y': res})
    return dict
    
def train(training_directory, cutoff):
    dict = {}
    vocab = create_vocabulary(training_directory, cutoff)
    dict.update({'vocabulary' : vocab})
    dict.update({'log prior' : prior(load_training_data(vocab, training_directory), ['2020', '2016'])})
    dict.update({'log p(w|y=2016)' : p_word_given_label(vocab, load_training_data(vocab, training_directory), '2016')})
    dict.update({'log p(w|y=2020)' :  p_word_given_label(vocab, load_training_data(vocab, training_directory), '2020')})
    return dict
    
   
def create_vocabulary(training_directory, cutoff):
    dict = {}
    words =[]
    retList = []
    for filename in os.listdir(training_directory):
        if(filename == '2016' or filename == '2020'):
            for subdir in os.listdir(training_directory + filename + '/'):
                each = open(training_directory + filename + '/'+ subdir, "r", encoding='utf-8').read().splitlines()
                words.extend(each)
    dict = Counter(words)
    for i in dict:
        if(dict[i] >= cutoff):
            retList.append(i)
    return sorted(retList)

def create_bow(vocab, filepath):
    words = []
    ret = {}
    words = open(filepath, "r", encoding='utf-8').read().splitlines()
    dict = Counter(words)
    for i in dict:
        if(i in vocab):
            ret.update({i : dict[i]})
        else:
            if None in ret:
                ret[None] = ret[None] + 1
            else:
                ret[None] = 1
    return ret

def load_training_data(vocab, directory):
    #listDir = os.listdir(directory)
    ret = []
    dict = {}
    for filename in os.listdir(directory):
        if(filename == '2016' or filename == '2020'):
            for subdir in os.listdir(directory + filename + '/'):
                dict = ({'label' : filename})
                dict.update({'bow' : create_bow(vocab, directory + filename + '/' + subdir)})
                ret.append(dict)
    return ret
"""
vocab = create_vocabulary('./corpus/training/', 2)
>>> training_data = load_training_data(vocab,'./corpus/training/')
>>> prior(training_data, ['2020', '2016'])
"""
def prior(training_data, label_list):
    c1 = 0
    c2 = 0
    dict = {}
    for label in training_data:
        if(label['label'] == "2016"):
            c1 = c1 + 1
        elif(label['label'] == "2020"):
            c2 = c2 + 1
    dict.update({"2020" : math.log(c2/(c1 + c2))})
    dict.update({"2016" : math.log(c1/(c1 + c2))})
    return dict

"""
vocab = create_vocabulary('./EasyFiles/', 1)
>>> training_data = load_training_data(vocab, './EasyFiles/')
>>> p_word_given_label(vocab, training_data, '2020')
"""
def p_word_given_label(vocab, training_data, label):
    dict = {}
    total = 0
    for i in range(len(vocab)):
        dict.update({vocab[i] : 1})
    dict.update({None : 1})
    #here dict with all values as 0
    for i in training_data:
        if(i['label'] == label):
            for j in i['bow']:
                dict[j] = dict[j] + i['bow'][j]
    for i in dict:
        total = total + dict[i]
    for i in dict:
        dict[i] = math.log(dict[i]/total)
    return dict

        
    
            