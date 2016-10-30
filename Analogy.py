import os
import gensim 
from gensim import corpora, models, similarities
from gensim.corpora import WikiCorpus, MmCorpus
from gensim.corpora import dictionary
import logging
from gensim.models.word2vec import BrownCorpus, Word2Vec
from gensim.models import Phrases
import nltk, os
from nltk.corpus import stopwords
import json
import nltk, shelve
from nltk.collocations import *
from sys import getsizeof
import pickle



path= "/media/savasy/e1c25d76-82c0-4d0b-bab6-ed427ad63556/home/savasy/Desktop/corpus/mtm/xmldata/"
analogyFile="analogy/questions_analogy3.txt"

def offset(pair):
 if pair[0] in model.vocab: 
  if pair[1] in model.vocab:
   return model[pair[0]] - model[pair[1]]
  else: 
   print(pair[1]+" missing")
   return []
 print(pair[0]+" missing")
 return []

def toStr(offs):
 s=""
 for o in offs:
  s=s+ ","+ str('%f' % o)
 return s


SIZE=300
modelName="sg0HS0Size"+str(SIZE)
model=Word2Vec.load(path+"models/"+modelName)



"""
w1-w2=  w3-w4

w1= w2+w3-w4 olmalı
w2= w1+w4-w3
w3= w1+w4-w2
w4= w2+w3-w1
"""



cor=0
incor=0
ilk5score=0


def check(w, wpred):
 global cor, incor, ilk5score
 if(wpred[0][0]==w):
  cor=cor+1
 else:
  incor=incor+1
 ilk5= [t[0] for t in wpred[:5]]
 if w in ilk5:
  ilk5score=ilk5score+1
 

cat=""
for line  in open(path+analogyFile):
 if line.startswith(":"):
  print("cor:", cor)
  print("incor:", incor)
  print("ilk5",ilk5score)
  cat=line
  print(cat)
  cor=0
  incor=0
  ilk5score=0
 else:
  try:
   w1,w2,w3,w4 = line.lower().strip().split()
   w1pred= model.most_similar(positive=[w2,w3], negative=[w4])
   w2pred= model.most_similar(positive=[w1,w4], negative=[w3])
   w3pred= model.most_similar(positive=[w1,w4], negative=[w2])
   w4pred= model.most_similar(positive=[w2,w3], negative=[w1])
   check(w1,w1pred)
   check(w2,w2pred)
   check(w3,w3pred)
   check(w4,w4pred)
  except KeyError as ee:
   print(ee)

print("cor:", cor)
print("incor:", incor)
print("ilk5",ilk5score)
