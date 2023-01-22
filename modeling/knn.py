import numpy as np

import pandas as pd
import joblib
from sklearn import metrics
from sklearn.model_selection import train_test_split#Import scikit-learn metrics module for accuracy calculation

X = joblib.load('X.joblib')
y = joblib.load('y.joblib')


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3,random_state=100)

classifier=KNeighborsClassifier(n_neighbors=7)
classifier.fit(x_train,y_train)
predictions = classifier.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

print("Accuracy:",metrics.accuracy_score(y_test, predictions))