import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import seaborn as sns
import random as rn
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


class PreProcessor:

    def __init__(self, df):
        self.df = df
        self.stopwords = None
        self.porter_stemmer = None
        self.wn_lemma = None
        self.testing_padded = None
    
    def dropping_null(self):
        self.df.dropna(axis=0, inplace=True)
    
    def droppping_duplicates(self):
        self.df.drop_duplicates(inplace=True)
    
    def clean(self, raw):
        """ Remove hyperlinks and markup """
        result = re.sub("<[a][^>]*>(.+?)</[a]>", 'Link.', raw)
        result = re.sub('&gt;', "", result)
        result = re.sub('&#x27;', "'", result)
        result = re.sub('&quot;', '"', result)
        result = re.sub('&#x2F;', ' ', result)
        result = re.sub('<p>', ' ', result)
        result = re.sub('</i>', '', result)
        result = re.sub('&#62;', '', result)
        result = re.sub('<i>', ' ', result)
        result = re.sub("\n", '', result)
        return result
    
    def remove_num(self, text):
        return re.sub(r'\d+', '', text)

    def deEmojify(self, x):
        regrex_pattern = re.compile(pattern = "["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)
        return regrex_pattern.sub(r'', x)

    def unify_whitespaces(self, x):
        return re.sub(' +', ' ', x)
    
    def remove_punctuation(self, text):
        return "".join(u for u in text if u not in ("?", ".", ";", ":",  "!",'"',','))

    def remove_symbols(self, x):
        if x is None:
            return ""
        return re.sub(r"[^a-zA-Z0-9?!.,]+", ' ', x)
    
    def settingStopwords(self):
        # nltk.download('stopwords')
        self.stopwords = set(stopwords.words("english"))
        self.porter_stemmer = nltk.PorterStemmer()

    def remove_stopword(self, text):
        text = [i.lower() for i in text.split() if i.lower() not in self.stopwords]
        return " ".join(text)

    def stemming(self, text):
        stemmed_word = [self.porter_stemmer.stem(i) for i in text]
        return ' '.join(stemmed_word)

    def cleaning(self, df, column):
        df[column] = df[column].fillna('')
        df[column] = df[column].apply(self.clean)
        df[column] = df[column].apply(self.deEmojify)
        df[column] = df[column].str.lower()
        df[column] = df[column].apply(self.remove_num)
        df[column] = df[column].apply(self.remove_symbols)
        df[column] = df[column].apply(self.remove_stopword)
        df[column] = df[column].apply(self.unify_whitespaces)
        df[column] = df[column].map(self.stemming)

        return df
    
    def preprocessing_pipeline(self):
        self.dropping_null()
        self.droppping_duplicates()
        self.settingStopwords()
        self.df = self.cleaning(self.df, 'Description')
        self.df = self.cleaning(self.df, 'Summary')

        max_length = 100
        vocab_size = 13000
        embedding_dim = 64
        trunc_type = "post"
        oov_tok = "<OOV>"
        padding_type = "post"

        tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
        tokenizer.fit_on_texts(self.df['Description'])

        word_index = tokenizer.word_index

        testing_sequences = tokenizer.texts_to_sequences(self.df['Description'])
        testing_padded = pad_sequences(testing_sequences, maxlen=max_length, padding=padding_type, 
                                       truncating=trunc_type)
        
        self.testing_padded = testing_padded
        return testing_padded
        