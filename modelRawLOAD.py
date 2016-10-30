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
modelName="sg1HS0Size"+str(SIZE)
model=Word2Vec.load(path+"models/"+modelName)


infile="/home/savasy/Dropbox/Deep Learning/SR_300Q.csv"
outfile="/home/savasy/Dropbox/Deep Learning/offsets/SR_300Q"+ modelName+".csv"

out=open(outfile,"w")
out.write("w1,w2,rel")
for i in range(1, SIZE+1):
 x=out.write(",V"+str(i))

out.write("\n")

for line in open(infile):
 line=line.strip().lower().split(",")
 w1 = line[0]
 w2 = line[1]
 rel=line[2]
 temp= toStr(offset((w1,w2)))
 if(temp):
  x=out.write(w1+","+w2+","+ rel+temp+"\n")

out.close()

