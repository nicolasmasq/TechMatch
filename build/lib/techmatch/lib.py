from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer

def load_vectorizer(filepath):
    #load vectorizer from pickle file
    return vectorizer


def load_classifier():
    #load model pickle from file
    return model

def df_cleaned(x):
    return x

def preprocessing(x):
# Define the features (data text) and target (tools name)
    # clean text
    x = df_cleaned(x)
    vectorizer = load_vectorizer()
    #vectorize text
    something_else = vectorizer.transform(x)
    return something_else

def predict(clean_data):
    model = load_classifier()
    prediction = model.predict()
    return prediction


if __name__ == '__main__':
    input = "vasljugfgsafjsgdflukdsfgvöudfg dsgfg uasugfulaskfjgv sdljfvg sl"
    clean_data = preprocessing()
    prediction = predict(clean_data)
