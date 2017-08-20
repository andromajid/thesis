import nltk
import re

def tokenize_and_stem(text, stemmer):
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(text)]
    filtered_tokens = []
    for token in tokens:
        if re.search("[a-zA-Z]", token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems

def tokenize_only(text):
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(text)]
    filtered_tokens = []
    for token in tokens:
        if re.search('a-zA-Z', token):
            filtered_tokens.append(token)
    return filtered_tokens