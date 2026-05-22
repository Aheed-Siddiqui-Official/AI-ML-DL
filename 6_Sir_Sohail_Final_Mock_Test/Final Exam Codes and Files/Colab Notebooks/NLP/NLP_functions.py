import NLP_functions as NLP
import re
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords

def lower_case(text):
  text = text.lower()
  return text
#-------------------------------------

def remove_punctuation(text):
  punctuation_pattern = r'[^\w\s]'
  text_cleaned = re.sub(punctuation_pattern, '', text)
  return text_cleaned
#----------------------------------

def remove_stopwords(text, language):
  stop_words = set(stopwords.words(language))
  text = text.lower()
  words_token = text.split()
  filtered_text = [word for word in words_token if word.lower() not in stop_words]
  filtered_text = " ".join(filtered_text)
  return filtered_text
#-------------------------------------
    
def remove_urls(text):
  url_pattern = re.compile(r"https?://\S+|www\.\S+")
  return url_pattern.sub(r"", text)
#-------------------------------------------

def html_remover(text):
  html_tags_pattern = re.compile(r"<.*?>")
  text_without_html_tags = re.sub(html_tags_pattern, "", text)
  return text_without_html_tags
#--------------------------------------------