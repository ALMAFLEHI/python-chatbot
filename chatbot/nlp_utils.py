import nltk
from nltk.tokenize import word_tokenize

def preprocess_text(text):
    """Basic text preprocessing with error handling"""
    try:
        tokens = word_tokenize(text.lower())
        return tokens
    except LookupError:
        nltk.download('punkt')
        return word_tokenize(text.lower())