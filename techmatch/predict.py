### THIS FILE CONTAINS ALL THE FUNCTIONS TO BE EXECUTED WHEN THE USER GIVES AN INPUT

import pickle
from techmatch.utils import preprocess

def load_vectorizer(filepath):
    #load vectorizer from pickle file
    with open(filepath,'rb') as file:
        vectorizer = pickle.load(file)
    return vectorizer


def load_classifier(filepath):
    #load model pickle from file
    with open(filepath,'rb') as file:
        model = pickle.load(file)
    return model


def predict(data, model):
    prediction = model.predict(data)
    preds = model.predict_proba(data)[0]
    labels = model.classes_
    tools = []
    label_preds = list(zip(labels, preds))
    sorted_label_preds = sorted(label_preds, key=lambda x: x[1], reverse=True)
    return sorted_label_preds


def predict_api(text):
    clean_data = preprocess(text)
    vectorizer = load_vectorizer("vectorizer.pkl")
    transformed_data = vectorizer.transform([clean_data])
    model = load_classifier("model.pkl")
    tools = predict(transformed_data, model)
    return tools

if __name__ == "__main__":
    predict_api("something something")
