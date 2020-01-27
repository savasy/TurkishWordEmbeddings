# TurkishWordEmbeddings


Python codes
- buildWordEmbedding.py : Too build Word embedding from texts in data folders
- buildOffsets.py:  The word pairs in Pairs.csv are converted into offsets
- Analogy.py: To answer analogy questions in fişe quesions_analogy3.txt
- Average.py: To aplly averaging model
- ann.py : Neural Network implementaiton 
- Sgd.py :  stochastic gradient descent Implementation 
- Projection.py: It learns a projeciton model from hyponym-hypernym pairs, then it maps a given hyponym to its hypernym. This code tests the approach with 10-fold cross validation. It uses hyp.csv file(that consist of pairs) and word embeddings. 
- buildOffsetsforMorphemes.py: It takes the embeddings for root and word formation and build offsets. It uses pairsForMorpology.txt file and morphemes.txt file. Finally it classify the morphemes. 


Word Embedding based Semantic Relation Detection for Turkish Language

We design a framework to automatically detect semantic relation for Turkish Language. The implementation is mostly done in Python Language. 

We also provide Turkish Word Embeedings for over 900k words, leaving inflected words as it is, e.g. söyledi, arabaların, öğrencilere.


There are two approaches implemeted here: One is classifiation and other is projection learning. They are part of two papers  as their abstracts follow


PAPER 1: Classification of Semantic Relation Pairs in Turkish Using Word Embeddings

Recent studies showed that neural network language models (NNLM) have been effectively and successfully applied to a variety of natural language processing (NLP) tasks.

One of the popular subjects is discovery of semantic and syntactic regularities. Word embedding representations are notably good at discovering such linguistic regularities that could be characterized by vector offsets.


In this paper, we propose a model utilizing word embedding offsets for automatic discovery of semantic relations that supports the researchers in building a lexicon. Although some studies use averaging the offsets, our proposed model uses rather entire training offsets and it is able to train classifier that successfully identifies semantic relations for a given word pair.

Our experiments showed that embedding offsets regarding semantic relations such as hypernym, meronym, synonym can be a easily separable and they can be considered a training data set at all. A model built on them can achieve a good separation. Therefore, the offsets can be simply turned into a classification problem. Afterwards, such semantic detection model might be transformed into a semantic generation model.


We conduct a variety of experiments on a huge amount of Turkish text. The word embedding vectors are trained 
by employing both continuous bag-of words (CBOW) and the skip-gram (SG) models  examining the effects of different setups with regard to the number of dimensions, training architecture, the amount of corpus and morphological analysis. We report that our design gives a very promising and successful results for Turkish Language.


PAPER 2: Learning Turkish Hypernymy Using Word Embeddings

Recently, Neural Network Language Models have been effectively applied to many types of Natural Language Processing (NLP) tasks. One popular type of task is discovery of semantic and syntactic regularities that support the researchers in building a lexicon. Word embedding representations are notably good at discovering such linguistic regularities. We argue that two supervised learning approaches based on word embeddings can be successfully applied to hypernym problem: Utilizing embedding offsets between word pairs and learning semantic projection to link the words. The offset-based model classifies offsets as hypernym or not. The semantic projection approach trains a semantic transformation matrix that ideally maps a hyponym to its hypernym. A semantic projection model can learn a projection matrix provided that there are a sufficient number of training word pairs. However, we argue that such models tend to learn is-a-particular hypernym relation rather than to generalize is-a relation. We conducted various experiments on a huge corpus in Turkish text. The embeddings are trained by applying both Continuous Bag-of Words and the Skip-Gram training models. The main contribution of the study is that the particular architecture is developed in order to apply word embedding approaches to Turkish language domain. We report that both projection model and offset classification model give promising and novel results for Turkish Language. 

PAPER 3: Exploiting Word Embeddings to Explore Inflectional Morphology in Turkish Language

Recently, unsupervisedly learned word embeddings have been successfully applied to many problems in NLP. Especially syntactic and semantic regularities can be implicitly encoded in word embeddings. In this study, we exploit word embeddings to explore inflectional morphology in Turkish Language. The language has rich and productive morphological structures such that one can generate theoretically infinite number of word forms from a nominal root. We argue that the offsets between the nominal root and its all formations encode morphological features and they can be discovered within supervised architectures. The goal is to disclose sequence of inflectional morphemes of a word through offsets. To reach the goal, the most popular embeddings algorithms were applied to huge amount of corpus to produce the embeddings and we showed that linear classifiers have a capacity of disclosing the inflectional morphemes through offsets. We present the study in detail with promising results and a variety of experiments in supervised architecture.

PAPER 4: IMPROVING WORD EMBEDDINGS PROJECTION FOR TURKISH HYPERNYM EXTRACTION
Turkish Journal of Electrical Engineering and Computer Science
2019 - SAVAŞ YILDIRIM -

Özet:Corpus-driven approaches can automatically explore is-a relations between the word pairs from corpus. This problem is also called hypernym extraction. Formerly, lexico-syntactic patterns have been used to solve hypernym relations. The language-specific syntactic rules have been manually crafted to build the patterns. On the other hand, recent studies have applied distributional approaches to word semantics. They extracted the semantic relations relying on the idea that similar words share similar contexts. Former distributional approaches have applied one-hot bag-of-word (BOW) encoding. The dimensionality problem of BOW has been solved by various neural network approaches, which represent words in very short and dense vectors, or word embeddings. In this study, we used word embeddings representation and employed the optimized projection algorithm to solve the hypernym problem. The supervised architecture learns a mapping function so that the embeddings (or vectors) of word pairs that are in hypernym relations can be projected to each other. In the training phase, the architecture first learns the embeddings of words and the projection function from a list of word pairs. In the test phase, the projection function maps the embeddings of a given word to a point that is the closest to its hypernym. We utilized the deep learning optimization methods to optimize the model and improve the performances by tuning hyperparameters. We discussed our results by carrying out many experiments based on cross-validation. We also addressed problem-specific loss function, monitored hyperparameters, and evaluated the results with respect to different settings. Finally, we successfully showed that our approach outperformed baseline functions and other studies in the Turkish language.

Anahtar Kelime:Projection learning, word embeddings, hypernym relation, deep learning






