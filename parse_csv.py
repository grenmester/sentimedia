import requests
import csv

def parse_csv(data_file):
    '''given a csv file containing sentiment data, returns a list of tuples containing the text and the sentiment'''
    r = requests.get(data_file)
    text = r.iter_lines(decode_unicode=True)
    reader = csv.reader(text, delimiter=',')

    data_list = []

    for row in reader:
        try:
            if row[1] == '0':
                sentiment = 'negative'
            else:
                sentiment = 'positive'

            pair = (row[3].strip(), sentiment)
            data_list.append(pair)
        except:
            pass

    return data_list
