import nltk

pos_tweets = [('I love this car', 'positive'),
              ('This view is amazing', 'positive'),
              ('I feel great this morning', 'positive'),
              ('I am so excited about the concert', 'positive'),
              ('He is my best friend', 'positive')]

neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative')]

test_tweets = [('I feel happy this morning', 'positive'),
('Larry is my friend', 'positive'),
('I do not like that man', 'negative'),
('My house is not great', 'negative'),
('Your song is annoying', 'negative')]

def process(tweets):
    processed_tweets = []
    for (words, sentiment) in tweets:
        words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
        processed_tweets.append((words_filtered, sentiment))
    return processed_tweets

tweets = process(pos_tweets+neg_tweets)

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

word_features = get_word_features(get_words_in_tweets(process(pos_tweets+neg_tweets)))

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

training_set = nltk.classify.apply_features(extract_features, tweets)

classifier = nltk.NaiveBayesClassifier.train(training_set)
