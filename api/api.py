from fastapi import FastAPI
from techmatch.predict import predict_api
from typing import List

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
