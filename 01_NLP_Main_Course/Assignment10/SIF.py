# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:19:09 2019

"""
import numpy as np
from sklearn.decomposition import PCA
from gensim.models import word2vec
from collections import Counter
import jieba

#def get_freq_table_from_model(model_path = './model/word2vec_v1.1.model'):
#    model = word2vec.Word2Vec.load(model_path)
#    counter = Counter()
#    for key, value in model.wv.vocab.items():
#        counter.update({key: value.count})
#    return counter

#vocab_counter = get_freq_table_from_model()



# A SIMPLE BUT TOUGH TO BEAT BASELINE FOR SENTENCE EMBEDDINGS
# Sanjeev Arora, Yingyu Liang, Tengyu Ma
# Princeton University
# convert a list of sentence with word2vec items into a set of sentence vectors
def SIF(sentence_list, model, a: float=1e-3, unlisted_word_freq=0.0001, skip_mode=False):
    '''
    Input:
        sentence_list: a list of tokenized sentences, text format
        a: param
        model: word2vec model object, pretrained by gensim
        embedding_size: word2vec model embedding size
    Output:
        SIF sentence embeddings
    '''
    
    vlookup = model.wv.vocab  # Gives us access to word index and count
    vectors = model.wv        # Gives us access to word vectors
    embedding_size = model.vector_size  # Embedding size

    vocab_count = 0
    for k in vlookup:
        vocab_count += vlookup[k].count # Compute the normalization constant Z (ALL Words Count)

    sentence_set = []
    for sentence in sentence_list:
        vs = np.zeros(embedding_size)  # add all word2vec values into one vector for the sentence
        sentence_length = len(sentence)
        for word in sentence:
            if word in vlookup:
                a_value = a / (a + vlookup[word].count / vocab_count)  # smooth inverse frequency, SIF
                vs = np.add(vs, np.multiply(a_value, vectors[word]))  # vs += sif * word_vector
            if word not in vlookup:
                a_value = a / (a + unlisted_word_freq)  # smooth inverse frequency, SIF
                vs = np.add(vs, np.multiply(a_value, np.zeros(embedding_size)))  # vs += sif * word_vector

        vs = np.divide(vs, sentence_length)  # weighted average

        sentence_set.append(vs)  # add to our existing re-calculated set of sentences

    # calculate PCA of this sentence set
    pca = PCA()
    pca.fit(np.array(sentence_set))
    u = pca.components_[0]  # the PCA vector
    u = np.multiply(u, np.transpose(u))  # u x uT

    # pad the vector?  (occurs if we have less sentences than embeddings_size)
    if len(u) < embedding_size:
        for i in range(embedding_size - len(u)):
            u = np.append(u, 0)  # add needed extension for multiplication below

    # resulting sentence vectors, vs = vs -u x uT x vs
    sentence_vecs = []
    for vs in sentence_set:
        sub = np.multiply(u,vs)
        sentence_vecs.append(np.subtract(vs, sub))

    return np.array(sentence_vecs)


if __name__ == "__main__":
    model = word2vec.Word2Vec.load('C:/Users/yihua/学习/开课吧NLP_course/my/Project01/model/word2vec_v1.1.model')
    
    sample_text = ["今天小明吃了一个包子，他觉得非常好吃。", "于是他又去买了一个包子，然后喂了狗。", "但是还不够爽，于是他又买了一笼包子。", "然后又喂了猫。"]
    sampt = [jieba.lcut(s) for s in sample_text]
    a = SIF(sampt, model)
