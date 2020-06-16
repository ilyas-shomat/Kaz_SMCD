import kaz_lang.helper as helper_kaz
import kaz_lang.twitter_helper as th_kaz


print('--------------------Test File------------------')



file  = open('../kaz_lang/files/stop_words', encoding='utf-8').read()

def get_stop_words_list(path):

    stop_words_list = []

    with open(path, 'r', encoding='utf-8') as file:

        for line in file:
            clear_line = line.replace("\n", '')
            stop_words_list.append(clear_line)

    return stop_words_list


# stop_words = get_stop_words_list('../kaz_lang/files/stop_words')
stop_words = helper_kaz.get_stop_words_list('../kaz_lang/files/stop_words')

print("file: " + str(stop_words))
print(stop_words)