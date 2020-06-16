import GetOldTweets3 as got
import foreign_langs.helper as helper
from collections import Counter


def get_tweets(key_word):
    print('please wait its loading .... ')
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(key_word) \
        .setSince("2018-01-01") \
        .setUntil("2020-06-15") \
        .setMaxTweets(100)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets


text = ""
text_tweets_list = get_tweets('black man die')
text_tweet_lenght = len(text_tweets_list)
# print(text_tweets_list)

for i in range(0, text_tweet_lenght):
    text = text_tweets_list[i][0] + " " + text

# print(text)
final_text = text
# print(final_text)

cleaned_text = helper.clean_text(text)

stop_words = helper.stop_words
final_words = helper.delete_stopwords(cleaned_text, stop_words)
emotion_list_from_text = helper.define_sentiment('files/emotions', final_words)


w = Counter(emotion_list_from_text)
helper.show_via_plt(w.keys(), w.values())


# print(final_words)
# print(emotion_list_from_text)