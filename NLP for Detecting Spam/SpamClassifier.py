import numpy
import pickle

import sklearn

def spamDetect(string):
    #Load in model
    filename = "spam_detection_classifier"
    spamclassifier = pickle.load(open(filename,'rb'))

    #Return prediction 
    return spamclassifier.predict(string)
