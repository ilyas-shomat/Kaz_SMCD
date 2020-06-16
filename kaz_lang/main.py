import kaz_lang.helper as helper_kaz
import kaz_lang.twitter_helper as th_kaz

main_text = ""
tweets = th_kaz.get_tweets_by_key_word('қылмыс', "2018-01-01", "2020-06-15", 30)
tweets_lengh = len(tweets)

# Main text taken from all tweets and merged for one big, now text without cleaning
main_text = helper_kaz.make_main_text_from_all_tweets(tweets, tweets_lengh)

cleaned_text = helper_kaz.clean_text(main_text)

stop_words = helper_kaz.get_stop_words_list('../kaz_lang/files/stop_words')

final_words = helper_kaz.delete_stop_words(cleaned_text, stop_words)


print(final_words)