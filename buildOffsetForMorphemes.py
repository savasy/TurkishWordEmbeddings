import numpy as np
import math
from sklearn.linear_model import SGDClassifier
from sklearn.neural_network import MLPClassifier
# random
import random 
from gensim.models.word2vec import BrownCorpus, Word2Vec

# classifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
# gensim modules
#http://linanqiu.github.io/2015/10/07/word2vec-sentiment/
from gensim import utils
from gensim.models.doc2vec import LabeledSentence
from gensim.models import Doc2Vec
from sklearn.metrics import confusion_matrix



path= "/media/savasy/e1c25d76-82c0-4d0b-bab6-ed427ad63556/home/savasy/Desktop/corpus/mtm/xmldata/"
SIZE=300

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

model=Word2Vec.load("/home/savasyildirim/Desktop/deepdene/tumSg1Dim300")
#model=Word2Vec.load(path+"models/"+modelName)

"""
    605 noun+a3sg+p2pl+acc
    584 noun+a3sg+p1pl+dat
"""

def buildCat(dosya):
 cats=[]
 for line in open(dosya):
  line=line.strip().split(" ")
  count= int(line[0])
  cat= line[1] 
  if count>500 and "noun+" in cat:
   cats.append(cat)
 return cats

   
cats=buildCat("morphemes.txt")

"""

load word and formations

 abidesi+abide+noun+a3sg+p3sg+nom
 abidesi’nde+abide+noun+a3sg+p3sg+apos+loc

"""

dosya= "pairsForMorpology.txt"
data=[]
for line in open(dosya):
 line = line.strip().split("+") 
 w1= line[0]
 w2=line[1]
 cat= "+".join(line[2:])
 if cat in cats and len(w2)>2 and w1 !=w2:
  data.append((w1,w2,cat))


train= [(offset((w1,w2)),cat) for w1,w2,cat in data]
train2= [t for t in train if t[0]!=[]]

"""
# Dosyaya Kaydetme
# kaydet
dosya="offsets.csv"
out=open(dosya, "w")

#header line
for i in range(300):
 x=out.write("V"+str(i)+",")

x=out.write("CLASS\n")

# vectors
for r in train2:
 x=out.write(toStr(r[0])[1:]+","+r[1]+"\n")

out.close()
"""



train3=[t[0] for t in train2]
label3=[t[1] for t in train2]


d=list(zip(train3,label3))

success=[]
for ii in range(0,3):
 random.shuffle(d)
 
 CUT=len(d)*5//10
 
 train_arrays= [i[0] for i in d[:CUT]]
 train_labels=[i[1] for i in d[:CUT]]
 
 test_arrays= [i[0] for i in d[CUT:]]
 test_labels= [i[1] for i in d[CUT:]]
 
 
 #clf = SVC()
 #clf.fit(train_arrays, train_labels)
 
 #clf = SGDClassifier()
 #clf.fit(train_arrays, train_labels)
 
 #q=clf.score(test_arrays, test_labels)
 #print(q)
 
  
 clf = LogisticRegression()
 clf.fit(train_arrays, train_labels)
 
 #clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(300, 300,300 ), random_state=1)
 #clf.fit(train_arrays, train_labels)
 
 sc=clf.score(test_arrays, test_labels)
 print(clf)
 print(sc)
 
 pr=clf.predict(test_arrays)
 real= test_labels
 print("confusion matrix")
 cm=confusion_matrix(pr, real)
 print(cm)
 success.append(sc)

print(sum(success)/ len(success))





