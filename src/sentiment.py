from config.configuration import db, col_chat, col_user, col_phrase
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')

def sentiment(phrases,character):
  print(character)
  polarity = []
  sia = SentimentIntensityAnalyzer()
  for elem in phrases:
    print(elem)
    element = sia.polarity_scores(elem["phrase"])
    element['phrase'] = elem['phrase']
    polarity.append(element)
  return polarity