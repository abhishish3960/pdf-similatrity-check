import re

def preprocess_text(text):
    # Remove any non-alphanumeric characters
    text = re.sub(r'\W+', ' ', text)
    return text.lower()
