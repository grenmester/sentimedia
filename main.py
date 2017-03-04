from training_data import messages
from analyze_sentiment import get_classifier, analyze
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html', test_string="I like food.")

@app.route('/sentiment')
def sentiment():
    classifier = get_classifier(messages)
    message = 'This is a good car'
    test = analyze(message, classifier)
    print(test)
    return render_template('index.html', test_string=test)

if __name__ == '__main__':
    app.run(debug=True)
