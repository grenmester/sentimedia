from flask import Flask, render_template, request
from training_data import training_messages
from analyze_sentiment import get_classifier, analyze
from comment_scrape import *
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('individual.html')

@app.route('/individual', methods=['POST'])
def individual():
    classifier = get_classifier(training_messages)
    url = request.form['video-url']
    print(url)
    video_comments = get_video_comments(url)
    comments_score = 0
    for comment in video_comments:
        comments_score += analyze(comment, classifier)
    normalized_score = comments_score / len(video_comments)

    return render_template('individual.html',
                           normalized_score = normalized_score,
                           url = url)

@app.route('/comparison')
def comparison():
    return render_template('comparison.html')

@app.route('/sentiment', methods=['POST'])
def sentiment():
    classifier = get_classifier(training_messages)
    message = request.form['message']
    test_sentiment = analyze(message, classifier)
    return render_template('index.html', test_sentiment=test_sentiment)

if __name__ == '__main__':
    app.run(debug=True)
