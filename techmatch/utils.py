# HERE WE PUT FUNCTIONS THAT ARE USED IN DIFFERENT TO AVOID DUPLICATIONS
# IN THE DIFFERENT CODES (predict.py, train.py...)

import string
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# CLEAN THE DATA - STEP 1
def preprocess_cleaning(sentence):
    sentence = sentence.lower()
    sentence = ''.join(char for char in sentence if not char.isdigit())

    for punctuation in string.punctuation:
        sentence = sentence.replace(punctuation, '')

    sentence = sentence.strip()
    sentence = re.sub(r'\s{2,}', ' ', sentence)
    sentence = re.sub(r'[’‘]', '', sentence)
    return sentence


# # CLEAN THE DATA - STEP 2
def preporocess_token(text):
  tokens = word_tokenize(text)
  stop_words = set(stopwords.words('english'))
  tokens_cleaned = [w for w in tokens if not w in stop_words]
  verb_lemmatized = [
  WordNetLemmatizer().lemmatize(word, pos = "v")
  for word in tokens_cleaned
  ]
  noun_lemmatized = [
  WordNetLemmatizer().lemmatize(word, pos = "n") # n --> nouns
  for word in verb_lemmatized
  ]
  final_text = " ".join(noun_lemmatized)

  return final_text

def preprocess(text):
    text = preprocess_cleaning(text)
    text = preporocess_token(text)
    return text
