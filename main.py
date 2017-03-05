from training_data import messages
from analyze_sentiment import get_classifier, analyze
from flask import Flask, render_template, request
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

@app.route('/sentiment', methods=['POST'])
def sentiment():
    classifier = get_classifier(messages)
    message = request.form['message']
    test_sentiment = analyze(message, classifier)
    return render_template('index.html', test_sentiment=test_sentiment)

if __name__ == '__main__':
    app.run(debug=True)
