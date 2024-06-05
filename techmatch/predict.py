### THIS FILE CONTAINS ALL THE FUNCTIONS TO BE EXECUTED WHEN THE USER GIVES AN INPUT

import pickle
from utils import preprocess

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
    for i in range(len(labels)):
        print(f"{labels[i]} - {preds[i]}")
    return prediction


if __name__ == '__main__':
    input = "marketing"
    clean_data = preprocess(input)
    v = load_vectorizer("vectorizer.pkl")
    print("vec loaded")
    [input_v] = v.transform([clean_data])
    model = load_classifier("model.pkl")
    print("model loaded")
    prediction = predict(input_v, model)
    print(prediction)
