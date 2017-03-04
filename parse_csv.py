import csv

def parse_csv(data_file):
    '''given a csv file containing sentiment data, returns a list of tuples containing the text and the sentiment'''
    with open(data_file, 'r', encoding="utf8") as csv_file:
        reader = csv.DictReader(csv_file)
        data_list = []

        for row in reader:
            try:
                if row['Sentiment'] == '0':
                    sentiment = 'negative'
                else:
                    sentiment = 'positive'

                pair = (row['SentimentText'].strip(), sentiment)
                data_list.append(pair)
            except:
                pass

    return data_list
