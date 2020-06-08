import string
from collections import Counter
import matplotlib.pyplot as plt
import foreign_langs.helper as helper

text  = open('files/read', encoding='utf-8').read()
# lower_case_text = text.lower()
# cleaned_text = lower_case_text.translate(str.maketrans('','', string.punctuation))
# splitted_text = cleaned_text.split()

final_text = helper.clean_text(text)
stop_words = helper.stop_words

final_words = helper.delete_stopwords(final_text, stop_words)



print(final_text)
print(stop_words)
print(final_words)


