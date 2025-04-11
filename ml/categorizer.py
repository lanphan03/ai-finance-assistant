import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import os
import joblib

MODEL_PATH = "ml/model.joblib"

class ExpenseCategorizer:
    def __init__(self):
        self.pipeline = None
        self.is_trained = False

    def train(self, data_path="data/expenses.csv"):
        df = pd.read_csv(data_path)
        df = df[df['Category'].notnull() & df['Description'].notnull()]

        if df.empty:
            print("Not enough data to train.")
            return

        X = df['Description']
        y = df['Category']

        self.pipeline = Pipeline([
            ('vectorizer', TfidfVectorizer()),
            ('classifier', MultinomialNB())
        ])

        self.pipeline.fit(X, y)
        self.is_trained = True
        self.save_model()
        print("Model trained and saved.")

    def predict(self, description):
        if not self.is_trained and not self.load_model():
            print("Model not available.")
            return None

        try:
            return self.pipeline.predict([description])[0]
        except Exception as e:
            print(f"Prediction error: {e}")
            return None

    def save_model(self):
        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
        joblib.dump(self.pipeline, MODEL_PATH)

    def load_model(self):
        if os.path.exists(MODEL_PATH):
            self.pipeline = joblib.load(MODEL_PATH)
            self.is_trained = True
            return True
        return False
