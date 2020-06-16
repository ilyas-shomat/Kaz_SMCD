from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import foreign_langs.twitter_analyses as tas
import foreign_langs.helper as helper
import matplotlib.pyplot as plt




text = tas.final_text
# cleaned_text = helper.clean_text(text)

def sentiment_analyses(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    pos = score['pos']
    neg = score['neg']
    neu = score['neu']

    if pos > neg:
        print('positive value')
    elif neg > pos:
        print('negative value')
    else:
        print('neutral')

sentiment_analyses(text)

# print(text)

