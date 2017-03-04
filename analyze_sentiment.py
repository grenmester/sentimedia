import nltk
from training_data import messages

def process(messages):
    '''given a lists of messages, splits the messages and deletes words with length less than 3'''
    processed_messages = []
    for (words, sentiment) in messages:
        words_filtered = [x.lower() for x in words.split() if len(x) >= 3]
        processed_messages.append((words_filtered, sentiment))
    return processed_messages

def get_word_features(processed_messages):
    '''given a list of processed messages, returns a list with words in order of freuqency'''
    all_words = []
    for (words, sentiment) in processed_messages:
        all_words.extend(words)

    word_list = nltk.FreqDist(all_words)
    word_features = word_list.keys()
    return word_features

def extract_features(document):
    '''given a list of strings, returns a dictionary indicating what words are contained in the input passed '''
    word_features = get_word_features(process(messages))
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

def get_classifier(messages):
    '''takes in training data in the form of a tuple containing a message and whether it is positive or negative and returns a classifier'''
    processed_messages = process(messages)
    training_set = nltk.classify.apply_features(extract_features, processed_messages)
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    return classifier

def analyze(message, classifier):
    '''takes in a message and a classifier and returns whether the classifier thinks it is positive or negative'''
    return classifier.classify(extract_features(message.split()))
