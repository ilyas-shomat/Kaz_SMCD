import string
import matplotlib as plt

def clean_text(text):

    lower_case_text = text.lower()
    cleaned_text = lower_case_text.translate(str.maketrans('', '', string.punctuation))
    splitted_text = cleaned_text.split()

    return splitted_text

def get_stop_words_list(path):

    stop_words_list = []

    with open(path, 'r', encoding='utf-8') as file:

        for line in file:
            clear_line = line.replace("\n", '')
            stop_words_list.append(clear_line)

    return stop_words_list

def delete_stop_words(splitted_text, stop_words):

    final_words = []

    for word in splitted_text:
        if word not in stop_words:
            final_words.append(word)

    return final_words

def make_main_text_from_all_tweets(tweets, len):

    text = ""

    for i in range(0, len):
        text = tweets[i][0] + " " + text

    return text

def show_via_plt(key, value):

    fig, ax1 = plt.subplots()
    ax1.bar(key, value)
    fig.autofmt_xdate()
    plt.savefig('graph.png')
    plt.show()