# SentiMedia

## Description

SentiMedia is a website which performs sentiment analysis on the comments section of any YouTube video. The user may submit any valid YouTube video link and the website will scrape through the comments section of that video, determine whether each comment is positive or negative, and return a score between -1 and 1 which indicates the sentiment of the comments section for that particular video. A score of -1 indicates that the comments section was very negative while a score of 1 indicates that the comments section was very positive. Users also have the option to compare the sentiment between two videos. There is also a table of channels listed along with their sentiment score, which is calculated by analyzing all the comments for the particular channel.

This website was created using Python's [Flask](http://flask.pocoo.org/) framework. The sentiment analysis was done with the help of Python's [NLTK](http://www.nltk.org/) (Natural Language Toolkit) library and is hosted by [Google App Engine](https://cloud.google.com/appengine/).

## Link

You can visit the website [here](https://nth-circlet-160511.appspot.com/).

## Credits

SentiMedia was created by Jacky Lee, Arkin Gupta, Terrence Ho, and Ryan Fong.
