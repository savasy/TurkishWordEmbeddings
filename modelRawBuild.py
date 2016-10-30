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

class MySentences():
 def __iter__(self):
  folders="2010 2011 2012 2013 2014".split()
  for fol in folders:
   for fileq in os.listdir(path+fol+"/"):
    if fileq.endswith("myparse2016"):
     print(fol+"/"+ fileq)
     for line in open(path+fol+"/"+ fileq):
      if len(line)> 10:
       yield nltk.wordpunct_tokenize(line)
       

sentences = MySentences() # a memory-friendly iterator
SG=1
HS=0
SIZES=[300]
for SIZE in SIZES:
 print("working for "+"models/PARSED/Parsed_sg"+str(SG)+"HS"+str(HS)+"Size"+str(SIZE))
 model = gensim.models.Word2Vec(sentences, size=SIZE, workers=50, sg=SG, hs=HS, min_count=10)
 model.init_sims(replace=True)
 model.save(path+"models/PARSED/Parsed_sg"+str(SG)+"HS"+str(HS)+"Size"+str(SIZE))



