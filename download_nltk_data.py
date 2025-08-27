import nltk
import os

# Create nltk_data directory inside your project if not exists
project_dir = os.path.dirname(__file__)
nltk_dir = os.path.join(project_dir, "nltk_data")
os.makedirs(nltk_dir, exist_ok=True)

# Download punkt and stopwords into that folder
nltk.download('punkt', download_dir=nltk_dir)
nltk.download('stopwords', download_dir=nltk_dir)

print("✅ punkt and stopwords downloaded into nltk_data/")
