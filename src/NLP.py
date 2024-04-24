import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score

def predict_review_sentiment(file_path: str):
  X, y = gather_data(file_path)
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
  classifier = train_classifier(X_train, y_train)
  evaluate_model(X_test, classifier, y_test)


def gather_data(file_path):
  nltk.download('stopwords')
  dataset = pd.read_csv(file_path, delimiter='\t', quoting=3)
  X, y = prepare_data(dataset)
  return X, y


def evaluate_model(X_test, classifier, y_test):
  y_pred = classifier.predict(X_test)
  cm = confusion_matrix(y_test, y_pred)
  print(cm)
  ac = accuracy_score(y_test, y_pred)
  print(ac)


def train_classifier(X_train, y_train):
  classifier = GaussianNB()
  classifier.fit(X_train, y_train)
  return classifier


def prepare_data(dataset):
  corpus = []
  nltk.download('stopwords')
  for index, elem in dataset.iterrows():
    review = clean_review(elem)
    corpus.append(review)
  cv = CountVectorizer(max_features=1500)
  X = cv.fit_transform(corpus).toarray()
  y = dataset.iloc[:, -1].values
  return X, y


def clean_review(elem):
  review = re.sub('[^a-zA-Z]', ' ', elem['Review'])
  review = review.lower()
  review = remove_stopwords(review)
  return review


def remove_stopwords(review):
  review = review.split()
  ps = PorterStemmer()
  all_stopwords = stopwords.words('english')
  all_stopwords.remove('not')
  review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
  review = ' '.join(review)
  return review