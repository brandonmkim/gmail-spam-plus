import pandas as pd 
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

#Access the dataset 
spam_data = pd.read_csv("spam_ham_dataset.csv")

x_data = spam_data["text"]

y_label = spam_data["label_num"]

#Splits dataset, 30% is for testing
x_train, x_test, y_train, y_test=train_test_split(x_data,y_label,test_size=0.3)

#Pipline to conver text into a vector then puts it through the  
pipe = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()),('clf', MultinomialNB())])

#Cross validation to tune hyperparameters 
gc = GridSearchCV(pipe,{'vect__ngram_range': [(1, 1), (1, 2)],'tfidf__use_idf': (True, False),'clf__alpha': (1e-2, 1e-3)})

#Training the model
model = gc.fit(x_train,y_train)

#Test Model
pred = model.predict(x_test)

np.mean(pred==y_test)

filename = 'spam_detection_classifier.sav'

pickle.dump(model,open(filename,'wb'))