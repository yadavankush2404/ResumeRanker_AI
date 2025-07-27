import re

def clean_text(text):
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower().strip()