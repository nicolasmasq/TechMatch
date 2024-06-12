from fastapi import FastAPI
from techmatch.predict import predict_api
from typing import List
import nltk

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

import nltk

nltk.download('punkt')

nltk.download('stopwords')

nltk.download('wordnet')

nltk.download('omw-1.4')

app = FastAPI()

# Define a root `/` endpoint
@app.get('/')
def index():
    #load a machine learning model
    #model.predict
   return {'ok': True}


@app.get('/tech_api')
def predict(text):    #  <=== "text" is the API params
    # Ml + prediction
    tools = predict_api(text)
    return {'tool': tools}
