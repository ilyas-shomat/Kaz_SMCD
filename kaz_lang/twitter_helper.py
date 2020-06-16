import GetOldTweets3 as got


def get_tweets_by_key_word(key_word, date_since, date_until, count):

    print('please wait its loading ..... ')

    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(key_word) \
        .setSince(date_since) \
        .setUntil(date_until) \
        .setMaxTweets(count)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets = [[tweet.text] for tweet in tweets]


    print('tweets loaded!!! ')
    return text_tweets


