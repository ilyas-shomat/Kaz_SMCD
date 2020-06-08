import string

def clean_text(text):

    text = open('files/read', encoding='utf-8').read()
    lower_case_text = text.lower()
    cleaned_text = lower_case_text.translate(str.maketrans('', '', string.punctuation))
    splitted_text = cleaned_text.split()

    return splitted_text