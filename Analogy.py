"""
Analogy.py

It is working for answering the question in question file

we check analogy question set just as applied in English Language designed by Mikolov 2013. They use syntactic analogy questions to demonstrate that the word vectors capture syntactic regularities. They are able to correctly answer almost 40\% of the questions. The datasets contain analogy questions of the form A-B = C- D, meaning that A is to B as C is to D, where the question is what would be the word D, as A,B and C given.

For Turkish Language, Sabanci Universitesi constructed and shared Turkish counterparts of those questions. The question set contains over 2K analogy tasks. They also apply their trained embeddings to answer the questions. We run our model on the same dataset and answer to the questions.

"""


import os
import gensim 
from gensim import corpora, models, similarities
from gensim.corpora import WikiCorpus, MmCorpus
from gensim.corpora import dictionary
import logging
from gensim.models.word2vec import BrownCorpus, Word2Vec
import nltk, shelve



SIZE=300
modelName="sg0HS0Size"+str(SIZE)
model=Word2Vec.load("models/"+modelName)
analogyFile="questions_analogy3.txt"

cor=0
incor=0
ilk3score=0


def check(w, wpred):
 global cor, incor, ilk3score
 if(wpred[0][0]==w):
  cor=cor+1
 else:
  incor=incor+1
 ilk3= [t[0] for t in wpred[:5]]
 if w in ilk3:
  ilk3score=ilk3score+1
 

cat=""
for line in open(analogyFile):
 if line.startswith(":"):
  if(cor +incor)!=0:
   print("correct answer:", cor)
   print("incorrrect answer:", incor)
   print("Success P@1: "+str(cor / (cor+ incor)))
   print("correct answers in first 3 :",ilk3score)
   print("Success P@3: "+str(ilk3score / (cor+ incor)))
   print("\n*****\n")
  cat=line
  print("...Working on the Category-> "cat)
  cor=0
  incor=0
  ilk3score=0
 else:
  try:
   w1,w2,w3,w4 = line.lower().strip().split()
   w4pred= model.most_similar(positive=[w2,w3], negative=[w1])
   check(w4,w4pred)
  except KeyError as ee:
   #print(ee)
   ee

print("correct answer:", cor)
print("incorrrect answer:", incor)
print("Success P@1: "+str(cor / (cor+ incor)))
print("correct answers in first 3 :",ilk3score)
print("Success P@3: "+str(ilk3score / (cor+ incor)))


