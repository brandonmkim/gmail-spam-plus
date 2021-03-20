import numpy
import pickle
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

import sklearn

def spamDetect(string):
    #Load in model
    filename = "spam_detection_classifier.sav"
    spamclassifier = pickle.load(open(filename,'rb'))
    test=[string]

    #Return prediction 
    return spamclassifier.predict_proba(test)[0][1],spamclassifier.predict(test)

