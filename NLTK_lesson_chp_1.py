# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 07:47:47 2015

@author: andrewstorey
"""

from nltk import *
nltk.download()
from nltk.book import *
#%%
#3.3 Collections and Bi-grams
list(bigrams(['more','is','said','than','done']))
text4.collocations()



#%%
text1
FreqDist([len(w) for w in text1]).plot(cumulative=True)
#%%
len(text1)
len(set(text1))
len(set(word.lower() for word in text1))
len(set(word.lower() for word in text1 if word.isalpha()))
#%%
word='cat'
if len(word)<5:
    print(word + ' is less then 5 characters long')
    
#%%
