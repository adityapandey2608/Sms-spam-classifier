📩 Spam vs Ham Detector

A machine learning–based Spam Message Classifier built with Flask.
The project uses NLP preprocessing, TF-IDF vectorization, and a trained RandomForest model to classify SMS messages as either Spam or Ham (Not Spam).

🚀 Features

✅ Classifies SMS messages as Spam or Ham

✅ Interactive web interface with Flask

✅ Preprocessing: tokenization, stopword removal, stemming

✅ Model trained using TF-IDF and multiple classifiers

✅ Final model stored as a pickle file for deployment

📂 Project Structure
Spam-Classifier/
│── app.py                # Flask app
│── spam_model.pkl        # Trained ML model
│── vectorizer.pkl        # TF-IDF Vectorizer
│── templates/
│   └── index.html        # Frontend HTML
│── static/
│   └── style.css         # CSS Styling
│── requirements.txt      # Dependencies
│── README.md             # Project documentation

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/spam-vs-ham.git
cd spam-vs-ham

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate    # For Windows
source venv/bin/activate # For Mac/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Flask App
python app.py


Then open in browser: http://127.0.0.1:5000/

📦 Deployment

You can deploy this project easily on:

🌐 Render

🌐 PythonAnywhere

🌐 Heroku

For deployment, add a Procfile:

web: gunicorn app:app

🧪 Example Messages

✉️ Spam:

"Claim your free vacation package today! Limited time offer."

"You have been selected for a $500 Amazon voucher. Call now!"

✉️ Ham:

"Hey, are we still meeting tomorrow?"

"Don't forget to bring your notebook to class."

📊 Model Performance

Algorithm tested: SVC, KNN, Naive Bayes, Decision Tree, Logistic Regression, RandomForest, AdaBoost, Gradient Boosting, XGBoost

✅ Best result: Multinomial Naive Bayes

👨‍💻 Author

Aditya Kumar Pandey
📎 www.linkedin.com/in/aditya-kumar-pandey10