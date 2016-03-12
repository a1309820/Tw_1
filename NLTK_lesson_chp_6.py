# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 13:32:23 2016

@author: andrewstorey
"""

import nltk


# Gender identification

def gender_features(word):
    features = {}
    features['first-letter'] = word[0].lower()
    features['preffix2']=word[:2].lower()
    features['suffix2']=word[-2:].lower()
    features['last-letter'] = word[-1].lower()
    features['length'] = len(word)
    return features

print(gender_features('Shrek'))

from nltk.corpus import names
labeled_names = ([(name, 'male') for name in names.words('male.txt')] + [(name,'female') for name in names.words('female.txt')])
import random
random.shuffle(labeled_names)


featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[5000:], featuresets[:5000]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(classifier.classify(gender_features('Neo')))
print(classifier.classify(gender_features('Andrew')))
print(classifier.classify(gender_features('Maki')))

print(nltk.classify.accuracy(classifier, test_set))


