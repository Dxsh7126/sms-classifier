import re

def normalize_obfuscation(text):
    replacements = {
        '0': 'o',
        '1': 'i',
        '3': 'e',
        '@': 'a',
        '$': 's'
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text


def preprocess_text(text):
    text = text.lower()
    text = normalize_obfuscation(text)
    text = re.sub(r'http\S+|www\S+', '<URL>', text)
    text = re.sub(r'\b\d{10,}\b', '<PHONE>', text)
    text = re.sub(r'[₹$£€]\s*\d+', '<MONEY>', text)
    return text
