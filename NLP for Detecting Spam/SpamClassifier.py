import numpy
import pickle

import sklearn

def spamDetect(string):
    #TODO create parser for the email
    
    #Load in model
    filename = "spam_detection_classifier"
    spamclassifier = pickle.load(open(filename,'rb'))

    #Make prediction 
    return spamclassifier.predict(string)
