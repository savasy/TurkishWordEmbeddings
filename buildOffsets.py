import os
import gensim 
from gensim import corpora, models, similarities
from gensim.corpora import WikiCorpus, MmCorpus
from gensim.corpora import dictionary
import logging
from gensim.models.word2vec import BrownCorpus, Word2Vec
from gensim.models import Phrases
import nltk, os

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
model=Word2Vec.load("models/"+modelName)

pairList="pairs.csv"
offsetOutFile="offsets/"+ modelName+".csv"


print("Offsets file will be "+offsetOutFile+"\n")

out=open(offsetOutFile,"w")
out.write("w1,w2,rel")
for i in range(1, SIZE+1):
 x=out.write(",V"+str(i))

out.write("\n")

for line in open(pairList):
 line=line.strip().lower().split(",")
 w1 = line[0]
 w2 = line[1]
 rel=line[2]
 temp= toStr(offset((w1,w2)))
 if(temp):
  x=out.write(w1+","+w2+","+ rel+temp+"\n")

out.close()

