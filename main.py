from flask import Flask, render_template, request, jsonify
from training_data import training_messages
from analyze_sentiment import get_classifier, analyze
from comment_scrape import get_video_comments, get_embed_id
import csv
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('individual.html')

@app.route('/individual')
def individual():
    return render_template('individual.html')

@app.route('/comparison')
def comparison():
    return render_template('comparison.html')

@app.route('/rankings')
def rankings():
    return render_template('rankings.html')

@app.route('/ajax', methods = ['POST'])
def ajax_request():
    classifier = get_classifier(training_messages)
    full_url = request.form['url']
    url = get_embed_id(full_url)

    video_comments = get_video_comments(full_url)
    comments_score = 0
    for comment in video_comments:
        comments_score += analyze(comment, classifier)
    normalized_score = comments_score / len(video_comments)

    return jsonify(url = url, normalized_score = normalized_score)

if __name__ == '__main__':
    app.run(debug=True)
