# -*- coding: utf-8 -*-
"""
Processing Raw Text
http://www.nltk.org/book/ch03.html

Created on Sat Oct  3 21:06:35 2015

@author: andrewstorey
"""


from nltk import *
import nltk, re, pprint
from nltk import word_tokenize
from BeautifulSoup import *
from __future__ import division  # Python 2 users only

#%%
# Import Crime and Punishment from Gutenburg project

import urllib2
url = "http://www.gutenberg.org/files/2554/2554.txt"
response = urllib2.urlopen(url)
raw = response.read()
type(raw)
len(raw)
raw[:100]
tokens = word_tokenize(raw)
len(tokens)
text = nltk.Text(tokens)
type(text)
text.collocations()
#%%

url='https://fstoppers.com/editorial/fstoppers-reviews-sony-alpha-a7rii-422mp-full-frame-camera-80386'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
print soup.prettify()[30000:60000]

#%%

r = urllib2.urlopen('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts').read()
soup = BeautifulSoup(r)
print type(soup)
print soup.prettify()[0:1000]

from IPython.display import HTML
HTML('<iframe src=http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts width=700 height=500></iframe>')
print soup.prettify()[28700:30500]
letters = soup.find_all("div", class_="ec_statements")
#%%

#3.4 Regular Expressions

wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
len(wordlist)

#words that end with ed:  ed$
edWords = [w for w in wordlist if re.search('ed$', w)]
edWords
len(edWords)

#words with 3rd j, 6th t and 8 letters long
[w for w in wordlist if re.search('^..j..t..$', w)]
sum(1 for w in wordlist if re.search('^..j..t..$',w))

#Telephone number words
[w for w in wordlist if re.search('^[wxyz][wxyz][wxyz][jkl]$', w)]
[w for w in wordlist if re.search('^[abc][ghi][def][mno]$', w)]

#Find words with two vowels in a row
wsj = sorted(set(nltk.corpus.treebank.words()))
fd = nltk.FreqDist(vs for word in wsj
                      for vs in re.findall(r'[aeiou]{2,}', word))
fd.most_common(50)
[w for w in wordlist if re.search('aia', w)]

#%%
#Finding Word Stems

def set(word):
    for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word
    
re.findall(r'^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')
re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')
re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processes')
re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$', 'language')
#%%
# Discovery of Hypernyms
# search for 'x and other y'
from nltk.corpus import brown
hobbies_learned = nltk.Text(brown.words(categories=['hobbies','learned']))
hobbies_learned.findall(r"<\w*> <and> <other> <\w*s>")
hobbies_learned.findall(r"<\w*> <as> <\w*s>")
#%%
# Normalizing Text

raw = """DENNIS: Listen, strange women lying in ponds distributing swords
      is no basis for a system of government.  Supreme executive power derives from
       a mandate from the masses, not from some farcical aquatic ceremony."""
wnl = nltk.WordNetLemmatizer()
[wnl.lemmatize(t) for t in word_tokenize(raw)]


