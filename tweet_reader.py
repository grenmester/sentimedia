import csv
def tweet():
    print ('start')
    csvfile = open('Sentiment_Analysis_Dataset.csv', 'r', encoding="utf8")
    #write_to = open('tweet.csv', 'w')
    reader = csv.DictReader(csvfile)
    #wr = csv.writer(write_to)
    data_list = []
    for row in reader:
        try:
        #print ", ".join(row)
            if row['Sentiment'] == '0':
                senti = 'negative'
            else:
                senti = 'positive'
            tup = (row['SentimentText'].strip(),senti)
            data_list.append(tup)
            #wr.writerow(tup)
            #print(tup)
        except:
            pass
    csvfile.close()
    #write_to.close()
    #write_to.close()
    print ('end')
    return data_list;

tweet()


