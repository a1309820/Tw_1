# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 07:47:47 2015

@author: andrewstorey
"""

from nltk import *
from nltk.book import *
#%%

corpus.gutenberg.fileids()

emma = corpus.gutenberg.words('austen-emma.txt')
len(emma)

#%%
from nltk.corpus import gutenberg
gutenberg.fileids()
emma = gutenberg.words('austen-emma.txt')
#%%
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)
    
#%%
#Web and Chat Text

from nltk.corpus import webtext

for fileid in webtext.fileids():
    print(fileid, webtext.raw(fileid)[:100], '...')

#%%
from nltk.corpus import brown
news_text = brown.words(categories='news')
fdist = FreqDist(w.lower() for w in news_text)
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    #print(m + ':', fdist[m], )
    print m, ':', fdist[m], '  ',

#%%
#conditional frequencies

cdf = ConditionalFreqDist(
           (genre, word)
           for genre in brown.categories()
           for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cdf.tabulate(conditions=genres, samples=modals)
#%%
from nltk.corpus import inaugural
cdf = ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america','citizen']
    if w.lower().startswith(target))
        
cdf.plot()
#%%
from __future__ import division

def lexical_diversity(my_text_data):
     word_count = len(my_text_data)
     vocab_size = len(set(my_text_data))
     diversity_score = vocab_size / word_count
     return diversity_score

t="This is a test"
lexical_diversity(t)

from nltk.corpus import genesis
lexical_diversity(genesis.words('english-kjv.txt'))

#%%
# WordNet
#  Let's find synonyms

from nltk.corpus import wordnet as wn

wn.synsets('motorcar')
wn.synset('car.n.01').lemma_names()

wn.synsets('dish')
#%%
#Word Hierarchy

motorcar=wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
types_of_motorcar[0]
sorted(lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas())

type(text1)