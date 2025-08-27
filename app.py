import nltk, os
nltk.data.path.append(os.path.join(os.path.dirname(__file__), "nltk_data"))

from flask import Flask, render_template, request
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

app = Flask(__name__)

# Load model and vectorizer
clf = pickle.load(open("spam_model.pkl", "rb"))
tfidf = pickle.load(open("vectorizer.pkl", "rb"))

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        transformed_sms = transform_text(message)
        vector_input = tfidf.transform([transformed_sms])
        result = clf.predict(vector_input)[0]

        if result == 1:
           prediction = "🚨 Spam Message Detected!"
           label = "spam"
        else:
           prediction = "✅ This is a Ham (Not Spam) message."
           label = "ham"

        return render_template('index.html', prediction=prediction, label=label, message=message)


if __name__ == "__main__":
    app.run(debug=True)
