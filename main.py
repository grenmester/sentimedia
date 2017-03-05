from flask import Flask, render_template, request, jsonify
from training_data import training_messages
from analyze_sentiment import get_classifier, analyze
from comment_scrape import get_video_comments, get_embed_id, get_channel_comments
import csv
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('logistics.html')

@app.route('/logistics')
def logistics():
    return render_template('logistics.html')

@app.route('/individual')
def individual():
    return render_template('individual.html')

@app.route('/comparison')
def comparison():
    return render_template('comparison.html')

@app.route('/graph')
def graph():
    return render_template('graph.html')

@app.route('/rankings')
def rankings():
    classifier = get_classifier(training_messages)
    list_of_channels = ["https://www.youtube.com/channel/UCpf42a3Bz4M9AdRDBXukneQ"]
    list_of_scores = []
    for channel in list_of_channels:
        comments = get_channel_comments(channel)
        score = 0
        for comment in comments:
            score += analyze(comment, classifier)
        normalized_score = score / len(comments)
        list_of_scores.append((channel, normalized_score))
    return render_template('rankings.html', list_of_scores = list_of_scores)

@app.route('/individual_ajax', methods = ['POST'])
def individual_ajax_request():
    classifier = get_classifier(training_messages)
    full_url = request.form['url']
    url = get_embed_id(full_url)

    video_comments = get_video_comments(full_url)
    comments_score = 0
    for comment in video_comments:
        comments_score += analyze(comment, classifier)
    normalized_score = comments_score / len(video_comments)

    return jsonify(url = url, normalized_score = normalized_score)

@app.route('/comparison_ajax', methods = ['POST'])
def comparison_ajax_request():
    classifier = get_classifier(training_messages)

    full_url_1 = request.form['url-1']
    url1 = get_embed_id(full_url_1)

    video_comments_1 = get_video_comments(full_url_1)
    comments_score_1 = 0
    for comment in video_comments_1:
        comments_score_1 += analyze(comment, classifier)
    normalized_score_1 = comments_score_1 / len(video_comments_1)

    full_url_2 = request.form['url-2']
    url2 = get_embed_id(full_url_2)

    video_comments_2 = get_video_comments(full_url_2)
    comments_score_2 = 0
    for comment in video_comments_2:
        comments_score_2 += analyze(comment, classifier)
    normalized_score_2 = comments_score_2 / len(video_comments_2)

    return jsonify(url1 = url1, url2 = url2, normalized_score_1 = normalized_score_1, normalized_score_2 = normalized_score_2)

if __name__ == '__main__':
    app.run(debug=True)
