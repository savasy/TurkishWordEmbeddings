import os, gensim, random
from gensim import corpora, models, similarities
from gensim.corpora import WikiCorpus, MmCorpus
from gensim.corpora import dictionary
from gensim.models.word2vec import BrownCorpus, Word2Vec
import numpy as np
from sklearn import linear_model
import math
from scipy import spatial


""" 
to project i-th column
"""
def getCol(array, i):
 col=[]
 for t in array:
  col.append(t[i])
 return col

"""
to find hypernym of given word 
"""
def findHyper(word):
 yp=[]
 for clf in clfList:
  yp.append(clf.predict([model[word]]))
 yp=np.transpose(yp)
 ms=mostSimilar(model, yp[0])
 return ms

"""
Compute Mean square error between two vectors
"""
def error(y1,y2):
 sum=0
 for t in zip(y1,y2):
  sum=sum + (t[0]-t[1]) * (t[0]-t[1]) 
 return math.sqrt( sum /len(y1))

"""
Cosine similairty , the most similar is to 1
"""
def cosine(x,y):
 return 1 - spatial.distance.cosine(x,y)

"""
model: deep learning word2vec model
vec a: given word vector
it returns the most similar word to given vec
"""
def mostSimilar(model, vec):
 max=0
 wordX=""
 for i in myvocab:
  c=cosine(vec,model[i][:SIZE])
  if c> max:
   max=c
   wordX=i
 return wordX

"""
clf List 
for a given xi vector 
project it into another vector that should be its hypenym vector
"""
def clfPredict(xi, clfList):
 yi=[ clf.predict(xi) for clf in clfList]
 return yi


""" loading word2vec model"""

SIZE=300
modelName="sg0HS0Size"+str(SIZE)
model=Word2Vec.load("models/"+modelName)



#pair list 
infile="hyp.csv"


# Training

pairs=[]

for line in open(infile):
 line=line.strip().lower().split(",")
 w1 = line[0]
 w2 = line[1]
 rel=line[2]
 if w1 in model.vocab and w2 in model.vocab:
  pairs.append((w1,w2,rel))


"""
  model deki vocanlari size 900K , dolayısıyla bendeki ufak vocablary yi kullanıyoruz.
"""
myvocab =[]
for line in open("vocab.txt"): 
 word=line.strip().lower()
 if word in model.vocab:
  myvocab.append(word)


random.shuffle(pairs)


boy=len(pairs)
K=10
slice=int(boy/K)

cntTopla=[]
testSizeTopla=[]

pWordsTopla=[]

error=[]

for i in list(range(0,boy, slice )):
 test= pairs[i:i+slice]
 #print("TEST:",test)
 train = [t for t in pairs if t not in test]
 #print("traİn",train)
 xvec=[]
 yvec=[]
 for w1,w2,rel in train:
  xvec.append(model[w1][:SIZE])
  yvec.append(model[w2][:SIZE])
 # test pair preparation
 xvecTest=[]
 yvecTest=[]
 for w1,w2,rel in test:
  xvecTest.append(model[w1][:SIZE])
  yvecTest.append(model[w2][:SIZE])
# yvec deki her bir boyut için clf uretiyoruz
# burda mesekla 300 tane clf var
# train
 clfList=[]
 for i in range(0,SIZE): 
  y=getCol(yvec,i)
  clf = linear_model.SGDRegressor(loss='epsilon_insensitive')
  qq=clf.fit(xvec, y)
  clfList.append(clf)
 yp=[]
 for clf in clfList:
  yp.append(clf.predict(xvecTest))
 yp=np.transpose(yp)
 pWords=[]
 for y in yp:
  ms=mostSimilar(model, y)
  pWords.append(ms)
  #print(ms)
 #for i in zip( test, pWords):
  #print(i)
 pWordsTopla=pWordsTopla+ pWords 
 cnt=0
 q=[]
 for i in zip( test, pWords):
  if(i[0][1]==i[1]): 
   #print(i)
   cnt=cnt+1
   q.append(i[1])
  else:
   error.append((i[0][1],i[1]))
 cntTopla.append(cnt)
 testSizeTopla.append(len(test))
 print("iterat,on : ",len(testSizeTopla))
 print("cnt", cnt)
 print("test size:",len(test))

print(sum(cntTopla)/sum(testSizeTopla)) 


