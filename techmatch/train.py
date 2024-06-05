### THIS FILE CONTAINS THE TRAIN MODEL

import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from utils import preprocess


filename_sm = "data/sales_tools - sales.csv"
filename_pm = "data/pm_tools - pm.csv"
filename_fin = "data/finance_tools - finance.csv"


def load_data(filename_sm, filename_pm, filename_fin):
    #load the data
    df_sm= pd.read_csv(filename_sm)
    df_pm= pd.read_csv(filename_pm)
    df_fin= pd.read_csv(filename_fin)
    df = pd.concat([df_sm, df_fin, df_pm], ignore_index=True)
    return df

def train_vectorizer(X):
    vectorizer = TfidfVectorizer()
    vectorizer.fit(X)
    with open("vectorizer.pkl", "wb") as file:
        pickle.dump(vectorizer, file)
    return vectorizer

def train_classifier(X_train, y_train):
    #Model Training
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    with open("model.pkl", "wb") as file:
        pickle.dump(model, file)
    return model

def evaluate(X_test, y_test, model):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test,y_pred)
    print("Accuracy:", accuracy)


if __name__  == "__main__":
    print("Load data")
    df = load_data(filename_sm, filename_pm,filename_fin)
    df = df.dropna()
    print("Data loaded")
    print(df.columns)
    print("Preprocess")
    X = df["Data Text"]
    X = X.apply(lambda x: preprocess(x))
    y = df["Tool name"]
    print("Train vectorizer")
    v = train_vectorizer(X)
    print("Vectorizer trained")
    X = v.transform(X)
    print("transformed")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print("Train model")
    model = train_classifier(X_train, y_train)
    print("Model trained")
    evaluate(X_test, y_test, model)
