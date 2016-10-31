
"""
Averaging MODEL of offsets 

Averaging function that computes mean of each semantic categories offsets by grouping them. Using mean vectors as a stable representation of a particular semantic relation, candidate pairs in hand are then evaluated on their cosine similarity closeness to those mean vectors. We use averaging method as baseline.

"""

from sklearn.linear_model import SGDClassifier
import random
from gensim.models.word2vec import BrownCorpus, Word2Vec
import math, nltk


"""
Input:  a list of vector of size -300 (liste)
Output: a single averaged vector


"""
def vecAvg(liste):
 size= len(liste[0])
 avgRes=[]
 for i in range(0,size):
  q= [w[i] for w in liste]
  avgRes.append(sum(q)/ len(q))
 return avgRes


"""
compute Euclidian distance between a and b
"""
def dist(a,b):
 return math.sqrt(sum([(t[0]- t[1])**2 for t in list(zip(a,b))]))


"""
To find the most similar vector in avgdict to qvec
return key of dictionary, such as hyp, syn, unrel
"""
def decide(avgdict, qvec):
 min=10000000000
 res="none"
 for k in avgdict.keys():
  disti= dist(qvec, avgdict[k])
  if(disti<min):
   min=disti
   res=k
 return res


"""
Offset file should have been produced by  buildOffsets.py
"""
offsetFile="offsets/sg0HS0Size300.csv"


data=[]
for line in open(offsetFile):
 if line.startswith("w1"):
  continue
 q= line.strip().split(",")
 data.append((q[2], [float(e) for e in q[3:]]))

keys= list( set([q[0] for q in data]))
mydict={}
for k in keys:
 mydict[k]=[]

for d in data:
 mydict[d[0]].append(d[1])

avgdict={}
for k in keys:
 avgdict[k]= vecAvg(mydict[k])

res= [(t[0], decide(avgdict, t[1])) for t in data]

print("confusion matrix:")
print("\t", end="")
print("\t".join(keys))

for k1 in keys:
 print(k1+"\t", end="")
 for k2 in keys:
  print(str(res.count((k1,k2))) +"\t", end="")
 print()

success=[t for t in res if t[0]==t[1]]

print()
print("success ratioe " + str(len(success))+"/ "+ str(len(res))+" : "+ str(len(success) / len(res)))


