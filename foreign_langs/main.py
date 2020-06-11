from collections import Counter
import foreign_langs.helper as helper

text  = open('files/read', encoding='utf-8').read()


final_text = helper.clean_text(text)
stop_words = helper.stop_words

final_words = helper.delete_stopwords(final_text, stop_words)

emotion_list_from_text = helper.define_sentiment('files/emotions', final_words)


print(emotion_list_from_text)
w = Counter(emotion_list_from_text)

helper.show_via_plt(w.keys(), w.values())




