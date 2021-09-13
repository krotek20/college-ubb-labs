import csv
import os

import numpy as np
import gensim
from sklearn import preprocessing, linear_model
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, silhouette_score
from sklearn.feature_extraction.text import CountVectorizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

from main import compute_train_validation


def feature_computation(model, data):
    features = []
    phrases = [phrase.split() for phrase in data]
    for phrase in phrases:
        vectors = [model[word] for word in phrase if (len(word) > 2) and (word in model.index_to_key)]
        if len(vectors) == 0:
            result = [0.0] * model.vector_size
        else:
            result = np.sum(vectors, axis=0) / len(vectors)
        features.append(result)
    return features


def train_supervised_model(train_features, encoded_train_outputs, validation_features, encoded_validation_outputs):
    classifier = linear_model.LogisticRegression()
    classifier.fit(train_features, encoded_train_outputs)
    encoded_computed_outputs = classifier.predict(validation_features)

    return accuracy_score(encoded_computed_outputs, encoded_validation_outputs)


def train_unsupervised_model(train_features, validation_features, encoded_validation_outputs):
    model = KMeans(n_clusters=2, init='k-means++', n_init=1, random_state=0, verbose=False, max_iter=300)
    model.fit(train_features)
    encoded_computed_outputs = model.predict(validation_features)
    return [accuracy_score(encoded_validation_outputs, encoded_computed_outputs),
            silhouette_score(train_features, model.labels_)]


crtDir = os.getcwd()
fileName = os.path.join(crtDir, 'reviews_mixed.csv')

data = []
with open(fileName) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            dataNames = row
        else:
            data.append(row)
        line_count += 1

inputs = [data[i][0] for i in range(len(data))]
outputs = [data[i][1] for i in range(len(data))]
labelNames = list(set(outputs))

TI, TO, VI, VO = compute_train_validation(inputs, outputs)
print()

encoder = preprocessing.LabelEncoder()
ETO = encoder.fit_transform(TO)
EVO = encoder.fit_transform(VO)

# Load Google's pre-trained Word2Vec
crtDir = os.getcwd()
modelPath = os.path.join(crtDir, 'models', 'GoogleNews-vectors-negative300.bin')
word2vecModel300 = gensim.models.KeyedVectors.load_word2vec_format(modelPath, binary=True)
WTF = feature_computation(word2vecModel300, TI)
WVF = feature_computation(word2vecModel300, VI)

# count vector
cv = CountVectorizer(analyzer='word')
cv.fit(inputs)
CTF = cv.transform(TI)
CVF = cv.transform(VI)

# word level tf-idf
vectorizer = TfidfVectorizer(max_features=5000, token_pattern=r'\w{1,}')
vectorizer.fit(inputs)
TTF = vectorizer.transform(TI)
TVF = vectorizer.transform(VI)

# ngram level tf-idf
vect_ngram = TfidfVectorizer(token_pattern=r'\w{1,}', ngram_range=(1, 2), max_features=5000)
vect_ngram.fit(inputs)
NTF = vect_ngram.transform(TI)
NVF = vect_ngram.transform(VI)

# supervised
print("SUPERVISED:")
# 1. count vector (bag of words)
print("Accuracy bag of words: ", train_supervised_model(CTF, ETO, CVF, EVO))
# 2. tf-idf
print("Accuracy tf-idf: ", train_supervised_model(TTF, ETO, TVF, EVO))
# 3. ngram
print("Accuracy ngram: ", train_supervised_model(NTF, ETO, NVF, EVO))
# 4. word2vec
print("Accuracy word2vec: ", train_supervised_model(WTF, ETO, WVF, EVO))

# unsupervised
print("UNSUPERVISED:")
# 1. count vector (bag of words)
metrics = train_unsupervised_model(CTF, CVF, EVO)
print("Accuracy bag of words: ", metrics[0])
print("Silhouette bag of words: ", metrics[1])
# 2. tf-idf
metrics = train_unsupervised_model(TTF, TVF, EVO)
print("Accuracy tf-idf: ", metrics[0])
print("Silhouette tf-idf: ", metrics[1])
# 3. ngram
metrics = train_unsupervised_model(NTF, NVF, EVO)
print("Accuracy ngram: ", metrics[0])
print("Silhouette ngram: ", metrics[1])
# 4. word2vec
metrics = train_unsupervised_model(WTF, WVF, EVO)
print("Accuracy word2vec: ", metrics[0])
print("Silhouette word2vec: ", metrics[1])
