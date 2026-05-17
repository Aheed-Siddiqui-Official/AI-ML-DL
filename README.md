<div align="center">
  <h1>🚀 AI-ML-DL</h1>
  <p><strong>My Personal AI, Machine Learning & Deep Learning Laboratory</strong></p>
  
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white" alt="Jupyter"/>
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=white" alt="TensorFlow"/>
  
  <br><br>
  <strong>From Hello World to Advanced Deep Learning • Clean • Reusable • Well Documented</strong>
</div>

---

## ✨ What's Inside

- Complete lecture notes with clear explanations
- Hands-on assignments and real-world projects
- **Reusable Code Snippets** — ready to use anytime
- Curated datasets for practice
- Personal experiments and model improvements

---

## 🧩 Reusable Code Snippets

### Common Imports
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
```

### Data Preprocessing
```python
# Fill missing values
df.fillna(df.median(numeric_only=True), inplace=True)
df['category'] = df['category'].fillna(df['category'].mode()[0])

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```
### Exploratory Data Analysis
```python
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Feature Correlation Heatmap')
plt.show()
```

### Machine Learning Model
```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

### Deep Learning (PyTorch)
```python
import torch
import torch.nn as nn

class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, num_classes)
        )
    
    def forward(self, x):
        return self.network(x)
```
### NLP Utilities
```python
import re
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text.strip()

# TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
```
### 📁 Folder Structure
```python
AI-ML-DL/
├── 0_Assignments & Projects/
├── 1_Python Lectures/
├── 2_OOP's/
├── 3_ML Lectures/
├── 4_NLP Lectures/
├── 5_Deep Learning/
├── DataSets/
├── Self/                    # Personal notes & experiments
├── .gitignore
└── README.md
```
<div align="center">
🔥 Actively maintained • Continuously improving • Learning in public
  
⭐ Star this repo

  Made with ❤️ by Aheed Siddiqui
</div>
