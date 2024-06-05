from fastapi import FastAPI
from techmatch.predict import predict_api

app = FastAPI()

# Define a root `/` endpoint
@app.get('/')
def index():
    #load a machine learning model
    #model.predict
    return {'ok': True}


@app.get('/tech_api')
def predict(text):
    # Ml + prediction
    tool = predict_api(text)
    return {'tool': tool}

