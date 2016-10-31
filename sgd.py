
"""
Applying SGD 
"""

from sklearn.linear_model import SGDClassifier
import random
from gensim.models.word2vec import BrownCorpus, Word2Vec

fileOffsets="offsets/sg0HS0Size300.csv"
            


data=[]

for line in open(fileOffsets):
 if line.startswith("w1"):
  continue
 q= line.strip().split(",")
 data.append((q[2], [float(e) for e in q[3:]]))

K=100
scores=[]

for i in range(1,K):
 random.shuffle(data)
 # Train and test
 cut= int(len(data)*2/3)
 train= data[:cut]
 test=data[cut:]



# divide y=f(x) OR y~ x vectors variable versus target vector

x_train= [t[1] for t in train]
y_train= [t[0] for t in train]

clf = SGDClassifier(loss="hinge", penalty="l2")
clf.fit(x_train, y_train)

x_test= [t[1] for t in test]
y_test= [t[0] for t in test]

predicted= clf.predict(x_test)
res=list(zip(y_test, predicted))
res2= [e for e in res if e[0]==e[1]]

scores.append(len(res2)/ len(res))

#print(scores)
print(fileOffsets)
print(sum(scores)/len(scores))







