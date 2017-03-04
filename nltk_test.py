import nltk

def process(messages):
    '''given a lists of messages, splits the messages and deletes words with length less than 3'''
    processed_messages = []
    for (words, sentiment) in messages:
        words_filtered = [x.lower() for x in words.split() if len(x) >= 3]
        processed_messages.append((words_filtered, sentiment))
    return processed_messages

def get_words_in_messages(processed_messages):
    '''given a list of processed messages, returns a list of all the words'''
    all_words = []
    for (words, sentiment) in processed_messages:
        all_words.extend(words)
    return all_words

def get_word_features(all_words):
    '''given a word list, returns a list with words in order of freuqency'''
    word_list = nltk.FreqDist(all_words)
    word_features = word_list.keys()
    return word_features

word_features = get_word_features(get_words_in_messages(process(messages)))

def extract_features(document):
    '''given a list of strings, returns a dictionary indicating what words are contained in the input passed '''
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

def get_classifier(messages):
    '''given a list of messages, returns a classifier trained by the messages'''
    processed_messages = process(messages)
    word_features = get_word_features(get_words_in_messages(processed_messages))
    training_set = nltk.classify.apply_features(extract_features, processed_messages)
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    return classifier
