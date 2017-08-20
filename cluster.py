from __future__ import print_function
import numpy as np
import pandas as pd
from nltk.stem.snowball import SnowballStemmer
import nltk
import file_operation.file
import os
import data_mining.cluster
file = os.path.dirname(os.path.realpath(__file__)) + "/access.log_2017-08-17_003600_2017-08-17_123600.log"

#load the nltk corpus english
stopwords = nltk.corpus.stopwords.words('english')

# load nltk's SnowballStemmer as variabled 'stemmer'
stemmer = SnowballStemmer("english")

total_data = len(stopwords)

total_stemmed = []
total_vocab = []
for chunk in file_operation.file.read_file_in_chunk(file):
    word_stemmed = data_mining.cluster.tokenize_and_stem(chunk, stemmer)
    total_stemmed.extend(word_stemmed)
    not_stemmed = data_mining.cluster.tokenize_only(chunk)
    total_vocab.extend(not_stemmed)

#adding panda to analyze the data
vocab_frame = pd.DataFrame({'WORD': total_vocab}, index=total_stemmed)
stemmed_frame = pd.DataFrame({'WORD': total_stemmed}, index=total_vocab)





