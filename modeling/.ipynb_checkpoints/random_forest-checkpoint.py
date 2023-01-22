"""
Random forest train file.
"""

import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


class TrainModel:


    def train_random_forest(X, y) -> str:

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
        rforest = RandomForestClassifier()
        rforest.fit(X_train, y_train)
        predictions = rforest.predict(X_test)

        print(classification_report(y_test, predictions))
        return "Completed"

X = joblib.load('qw.joblib')
y = joblib.load('er.joblib')
RANDOM_FOREST = TrainModel.train_random_forest(X=X, y=y)
