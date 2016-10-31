import os, nltk
import gensim 
from gensim import corpora, models, similarities
from gensim.corpora import WikiCorpus, MmCorpus
from gensim.corpora import dictionary
import logging
from gensim.models.word2vec import Word2Vec
from gensim.models import Phrases


path="data/"


class MySentences():
 def __iter__(self):
  folders="2010".split()
  for fol in folders:
   for fileq in os.listdir(path+fol+"/"):
    if fileq.endswith(".txt"):
     print(fol+"/"+ fileq)
     for line in open(path+fol+"/"+ fileq):
      if len(line)> 10:
       yield nltk.wordpunct_tokenize(line)
       

sentences = MySentences() # a memory-friendly iterator
SG=0
HS=0
SIZE=300

print("working for sg"+str(SG)+"HS"+str(HS)+"Size"+str(SIZE))
model = gensim.models.Word2Vec(sentences, size=SIZE, workers=10, sg=SG, hs=HS, min_count=5)
model.init_sims(replace=True)
model.save("models/sg"+str(SG)+"HS"+str(HS)+"Size"+str(SIZE))



