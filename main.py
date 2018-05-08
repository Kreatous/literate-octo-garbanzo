import sys, tweepy, json, nltk.classify.util
from tweepy import Cursor
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names

positive_vocab = [ 'awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)' ]
negative_vocab = [ 'bad', 'terrible','useless', 'hate', ':(' ]
neutral_vocab = [ 'movie','the','sound','was','is','actors','did','know','words','not' ]

def check_word(word, list):
    if word in list:
        return list

def word_feats(words):
    return dict([(word, True) for word in words])

if __name__ == "__main__":

	auth = tweepy.OAuthHandler(consumer_key='V987DRZmMDTuGv8qXwpPDQ',
		consumer_secret='YRyMcRI9xjaGb6UG5B8WC8pMY0G5ATZ5n1ObO7uAjjo')

	auth.set_access_token('869223589-3zpYLDRAsuz6RgLqUmvdGFDrmDLGVg12XBRqZC4J',
		'ezkHcbBYfcmfH4Y9T6zhH4FHVxRQZhMsfiW1tFJZ0')

	api = tweepy.API(auth)

	#api.user_timeline('bloombergtv')


	#item = api.get_user('twitter')
	#print(item.screen_name)


	positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
	negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
	neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]
	 
	train_set = negative_features + positive_features + neutral_features
	 
	classifier = NaiveBayesClassifier.train(train_set) 


	for status in Cursor(api.user_timeline, id='bloombergtv').items(200):
		neg = 0
		pos = 0
		if 'apple' in status.text.lower():
			sentence = status.text.lower()
			words = sentence.split(' ')

			for word in words:
				classResult = classifier.classify( word_feats(word))
				if classResult == 'neg':
					neg = neg + 1
				if classResult == 'pos':
					pos = pos + 1

			print(status.text)
			print('Positive: ' + str(float(pos)/len(words)))
			print('Negative: ' + str(float(neg)/len(words)))
