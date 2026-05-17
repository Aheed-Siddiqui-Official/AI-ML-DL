import re, nltk
from nltk.corpus import stopwords

# Lowercase
def lowercase_text(text):
    return text.lower()

# Remove Punctuation
def remove_punctuation(text):
    punctuation_pattern = r'[^\w\s]'
    cleaned_text = re.sub(punctuation_pattern, '', text)
    return cleaned_text

print(stopwords.words("english"))

# Remove Stopwords
def remove_stopwords(text, language='english'):
    text = text.lower() 
    stop_words = set(stopwords.words(language))
    word_tokens = text.split()
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return ' '.join(filtered_text)

# Remove URLS
def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub('', text)

# Remove HTML Tags
def remove_html_tags(text):
    html_pattern = r'<.*?>'
    return re.sub(html_pattern, '', text)


def clean_text(text, language='english', remove_stop=True, 
               remove_punct=True, remove_url=True, remove_html=True):
    
    if remove_html:
        text = remove_html_tags(text)
    
    if remove_url:
        text = remove_urls(text)
    
    if remove_punct:
        text = remove_punctuation(text)
    
    if remove_stop:
        text = remove_stopwords(text, language)
    else:
        text = lowercase_text(text)
    
    return text.strip()

if __name__ == "__main__":
    sample_text = """<html><div>
    <h1>Hello World!</h1>
    <p>This is a sample sentence, and we are going to remove the stopwords from this. 
    Visit https://example.com for more info.</p>
    </div></html>"""
    
    print("Original Text:")
    print(sample_text)
    print("\n" + "="*60 + "\n")
    
    # Individual functions
    print("1. Lowercase:")
    print(lowercase_text(sample_text))
    
    print("\n2. Remove Punctuation:")
    print(remove_punctuation(sample_text))
    
    print("\n3. Remove Stopwords:")
    print(remove_stopwords(sample_text))
    
    print("\n4. Remove URLs:")
    print(remove_urls(sample_text))
    
    print("\n5. Remove HTML Tags:")
    print(remove_html_tags(sample_text))
    
    print("\n6. Full Cleaning Pipeline:")
    cleaned = clean_text(sample_text, language='english')
    print(cleaned)

text = "Hello, World! This is a test https://google.com <b>bold</b>"

print(clean_text(text))                    # Full cleaning of sentence
print(clean_text(text, remove_stop=False)) # Without removing stopwords from sentence