# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 20:12:00 2015

@author: andrewstorey
"""

from nltk import *
from __future__ import division  # Python 2 users only
import nltk, re, pprint
from BeautifulSoup import *
#%%
# Categorizing and Tagging Words
text = word_tokenize('And now for something completely different')
nltk.pos_tag(text)
nltk.help.upenn_tagset('RB')

text2 = word_tokenize('They refuse to permit us to obtain a refuse permit')
nltk.pos_tag(text2)


# find similarily used words eg: for w find w1 w w2  -> w1 w' w2
text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
text.similar('woman')
text.similar('jump')

# POS -> Part-of-Speach
pos={}
pos
pos['colorless']
pos['ideas'] = 'N'
pos['sleep'] = 'V'
pos['furiously'] = 'ADV'
pos
list(pos)
sorted(pos)
[w for w in pos if w.endswith('s')]
for word in sorted(pos):
    print(word + " : " + pos[word])
    
type(text1)
#%%

from nltk.corpus import brown
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
tag_fd.most_common()
tag_fd.plot(cumulative=True)

#%%
# Let's see what words come before nouns

word_tag_pairs = nltk.bigrams(brown_news_tagged)
noun_preceders = [a[1] for (a,b) in word_tag_pairs if b[1]=='NOUN']
fdist = nltk.FreqDist(noun_preceders)
fdist.most_common()

#%%
# What are the most common verbs in the news text?

wsj = nltk.corpus.treebank.tagged_words(tagset='universal')
word_tag_fd = nltk.FreqDist(wsj)
[wt[0] for (wt,_) in word_tag_fd.most_common() if wt[1]=='VERB']
verbs = [a for (a,b) in wsj if b=='VERB']
nltk.FreqDist(verbs).most_common(20)

#%%
#Words that follow 'often'
brown_learned_text = brown.words(categories='learned')
sorted(set (b for (a,b) in nltk.bigrams(brown_learned_text) if a=='often'))

brown_lrnd_tagged = brown.tagged_words(categories='learned', tagset='universal')
tags = [b[1] for (a,b) in nltk.bigrams(brown_lrnd_tagged) if a[0]=='often']
nltk.FreqDist(tags).tabulate()

#%%
#Now find particular structures of phrases eg. verb to verb
from nltk.corpus import brown
def process(sentence):
    for (w1, t1), (w2, t2), (w3, t3) in nltk.trigrams(sentence):
        if(t1.startswith('V') and t2=='TO' and t3.startswith('V')):
            print(w1, w2, w3)
            
for tagged_sent in brown.tagged_sents():
    process(tagged_sent)
    
#%%
# Lets find highly ambigious words.

brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
data = nltk.ConditionalFreqDist((word.lower(), tag) 
                                for (word, tag) in brown_news_tagged)
for word in sorted(data.conditions()):
    if len(data[word])>3:
        tags = [tag for (tag, _) in data[word].most_common()]
        print(word, ' '.join(tags))

#%%
# Dictionaries in Python

pos={}
print(pos)

pos['colourless']='ADJ'
print(pos)

pos['ideas']='N'
pos['sleep']='V'
pos['furiously']='ADV'
print(pos)
print(pos['ideas'])

print(list(pos))
print(sorted(pos))
print([w for w in pos if w.endswith('s')])

print(list(pos.keys()))
print(list(pos.values()))
print(list(pos.items()))
for key, val in sorted(pos.items()):
    print(key + " : " + val)

#%%
#Default dictionaries
from collections import defaultdict
pos = defaultdict(lambda: 'NOUN')
pos['colorless'] = 'ADJ'
pos['blog']
list(pos.items())
#%%
#Lookup Tagger
fd=nltk.FreqDist(brown.words(categories='news'))
cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
most_freq_words=fd.most_common(100)
likely_tags = dict((word, cfd[word].max()) for (word,_) in most_freq_words)
baseline_tagger = nltk.UnigramTagger(model=likely_tags)
baseline_tagger.evaluate(brown_tagged_sents)

