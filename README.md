# TurkishWordEmbeddings


Python codes
- buildWordEmbedding.py : Too build Word embedding from texts in data folders
- buildOffsets.py:  The word pairs in Pairs.csv are converted into offsets
- Analogy.py: To answer analogy questions in fişe quesions_analogy3.txt
- Average.py: To aplly averaging model
- ann.py : Neural Network implementaiton 
- Sgd.py :  stochastic gradient descent Implementation 



Word Embedding based Semantic Relation Detection for Turkish Language

We design a framework to automatically detect semantic relation for Turkish Language. The implementation is mostly done in Python Language. 

We also provide Turkish Word Embeedings for over 900k words, leaving iflected words as it is, e.g. söyledi, arabaların, öğrencilere.



Abtract of the study

Recent studies showed that neural network language models (NNLM) have been effectively and successfully applied to a variety of natural language processing (NLP) tasks.

One of the popular subjects is discovery of semantic and syntactic regularities. Word embedding representations are notably good at discovering such linguistic regularities that could be characterized by vector offsets.


In this paper, we propose a model utilizing word embedding offsets for automatic discovery of semantic relations that supports the researchers in building a lexicon. Although some studies use averaging the offsets, our proposed model uses rather entire training offsets and it is able to train classifier that successfully identifies semantic relations for a given word pair.

Our experiments showed that embedding offsets regarding semantic relations such as hypernym, meronym, synonym can be a easily separable and they can be considered a training data set at all. A model built on them can achieve a good separation. Therefore, the offsets can be simply turned into a classification problem. Afterwards, such semantic detection model might be transformed into a semantic generation model.


We conduct a variety of experiments on a huge amount of Turkish text. The word embedding vectors are trained 
by employing both continuous bag-of words (CBOW) and the skip-gram (SG) models  examining the effects of different setups with regard to the number of dimensions, training architecture, the amount of corpus and morphological analysis. We report that our design gives a very promising and successful results for Turkish Language.
