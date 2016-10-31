
"""
Applying ANN 
"""
from sklearn.neural_network import MLPClassifier
import random
from gensim.models.word2vec import BrownCorpus, Word2Vec

def offset(pair):
 if pair[0] in model.vocab: 
  if pair[1] in model.vocab:
   return model[pair[0]] - model[pair[1]]
  else: 
   print(pair[1]+" missing")
   return []
 print(pair[0]+" missing")
 return []


fileOffsets="offsets/sg0HS0Size300.csv"

data=[]
for line in open(fileOffsets):
 if line.startswith("w1"):
  continue
 q= line.strip().split(",")
 data.append((q[:3], [float(e) for e in q[3:]]))

scores=[]

#for i in range(1,K):
#random.shuffle(data)

pairs=[ e[0][0:2] for e in data ]
data=[ (e[0][2], e[1]) for e in data ]

# Train and test
cut= int(len(data)*2/3)
train= data[:cut]
test=data[cut:]

pairsTest=pairs[cut:]




# divide y=f(x) OR y~ x vectors variable versus target vector

x_train= [t[1] for t in train]
y_train= [t[0] for t in train]

# clf = SGDClassifier(loss="hinge", penalty="l2")
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(150, ), random_state=1)
clf.fit(x_train, y_train)

x_test= [t[1] for t in test]
y_test= [t[0] for t in test]

predicted= clf.predict(x_test)
res=list(zip(y_test, predicted))
res2= [e for e in res if e[0]==e[1]]

scores.append(len(res2)/ len(res))

#print(scores)
print("file:"+fileOffsets)
print(sum(scores)/len(scores))

print("SCORE:"+str(scores))




"""
import nltk
print(nltk.FreqDist( list(predicted)))

errorAnalysis= zip(pairsTest, y_test, predicted)
for e in errorAnalysis:
 print(e[0], e[1], e[2], e[1]==e[2])
"""




"""
Language Generation

import os
import gensim 
from gensim import corpora, models, similarities

path= "/media/savasy/e1c25d76-82c0-4d0b-bab6-ed427ad63556/home/savasy/Desktop/corpus/mtm/xmldata/"
SIZE=300
modelName="sg1HS0Size"+str(SIZE)
model=Word2Vec.load(path+"models/"+modelName)

word="hayvan"

pairGen=[(word,can) for can in list(model.vocab)[0:500000]]
x_test_gen=[offset(p) for p in pairGen]
predicted= clf.predict(x_test_gen)

for k1,rel in zip(pairGen, predicted):
 if rel == "hyp":
  print(k1,rel)
"""




"""
Lexial Memory için


from sklearn.linear_model import SGDClassifier
import random
from gensim.models.word2vec import BrownCorpus, Word2Vec



dosyamTest= "/home/savasyildirim/Dropbox/Deep Learning/offsets/memorization/TEST3_sg1HS0Size300.csv"
dosyamTrain="/home/savasyildirim/Dropbox/Deep Learning/offsets/memorization/TRAIN3_sg1HS0Size300.csv"

data=[]

for line in open(dosyamTest):
 if line.startswith("w1"):
  continue
 q= line.strip().split(",")
 data.append((q[2], [float(e) for e in q[3:]]))


test= data

data=[]

for line in open(dosyamTrain):
 if line.startswith("w1"):
  continue
 q= line.strip().split(",")
 data.append((q[2], [float(e) for e in q[3:]]))


train= data



x_train= [t[1] for t in train]
y_train= [t[0] for t in train]

clf = SGDClassifier(loss="hinge", penalty="l2")
clf.fit(x_train, y_train)

x_test= [t[1] for t in test]
y_test= [t[0] for t in test]

predicted= clf.predict(x_test)
res=list(zip(y_test, predicted))
res2= [e for e in res if e[0]==e[1]]

print(len(res2)/ len(res))


"""






