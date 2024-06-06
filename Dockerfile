FROM python:3.10.6-buster

COPY api /api
COPY requirements.txt /requirements.txt
COPY techmatch /techmatch
COPY setup.py /setup.py


RUN pip install --upgrade pip
#RUN pip install -r requirements.txt
RUN pip install .

RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader wordnet
RUN python -m nltk.downloader omw-1.4

CMD uvicorn api.api:app --host 0.0.0.0
