#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/16
# @Author : YKP

from pathlib import Path
import os
import MeCab
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

mt = MeCab.Tagger("-Owakati")

def feature_extractor(case='bagofwords', max_df=1.0, min_df=0.0):

    if case == 'tfidf':
        vectorizer = TfidfVectorizer(token_pattern='\w', ngram_range=(1,2), max_df=max_df, min_df=min_df)
    if case == 'bagofwords':
        vectorizer = CountVectorizer(analyzer='char_wb', ngram_range=(2, 2), max_df=max_df, min_df=min_df)

    return vectorizer

def tokenize(text):
    return mt.parse(text)

def load_data(base_path):
    
    data = []
    label = []
    
    y = 0
    for root, dirs, files in os.walk(Path(__file__).parent / base_path):
        for f in files:
            with open(os.path.join(root, f), "r",encoding='utf8') as f:
                for line in f.readlines():
                    data.append(tokenize(''.join(line)))
                    # label.append(root.split('/')[-1])
                    label.append(np.array(y))
        y += 1
    
    vectorizer = feature_extractor(case='tfidf')
    data = vectorizer.fit_transform(data)
    
    # print(data.shape)
    
    return data.todense(), label
    
if __name__ == '__main__':
    
    base_path = './data'
    
    data, label = load_data(base_path)
    print(data, label)