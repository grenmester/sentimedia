from parse_csv import parse_csv

training_messages = parse_csv("https://storage.googleapis.com/sentiment-analysis-dataset/training_data.csv")
training_messages = training_messages[:500]
