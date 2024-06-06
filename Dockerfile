FROM python:3.10.6-buster

COPY techmatch/api /api
COPY requirements.txt /requirements.txt
COPY model.pkl /model.pkl
COPY vectorizer.pkl /vectorizer.pkl
COPY techmatch /techmatch
COPY setup.py /setup.py


RUN pip install --upgrade pip
#RUN pip install -r requirements.txt
RUN pip install .

CMD uvicorn techmatch.api.api:app --host 0.0.0.0 --port $PORT
