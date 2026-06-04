import streamlit as st
import pickle
import numpy as np

# Try different imports for model loading
try:
    from tensorflow.keras.models import load_model
    from tensorflow.keras.preprocessing.sequence import pad_sequences
except ImportError:
    try:
        from keras.models import load_model
        from keras.preprocessing.sequence import pad_sequences
    except ImportError:
        st.error("Please install tensorflow or keras: pip install tensorflow")
        st.stop()

# Set page configuration
st.set_page_config(
    page_title="Next Word Predictor",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.1em;
        margin-bottom: 30px;
    }
    .prediction-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
    }
    .info-box {
        background-color: #e8f4f8;
        padding: 15px;
        border-radius: 8px;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Load model and tokenizer
@st.cache_resource
def load_resources():
    try:
        model = load_model('lstm_model.h5')
        with open('tokenizer.pkl', 'rb') as f:
            tokenizer = pickle.load(f)
        with open('max_len.pkl', 'rb') as f:
            max_len = pickle.load(f)
        return model, tokenizer, max_len
    except FileNotFoundError as e:
        st.error(f"❌ Error: Could not find required file - {e}")
        return None, None, None

# Load resources
model, tokenizer, max_len = load_resources()

if model is None:
    st.error("Could not load model. Please ensure all files (lstm_model.h5, tokenizer.pkl, max_len.pkl) are in the same directory.")
    st.stop()

# Main UI
st.markdown('<div class="main-header">🔮 Next Word Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">LSTM-powered Text Prediction</div>', unsafe_allow_html=True)

# Sidebar information
with st.sidebar:
    st.header("📋 Information")
    st.info("""
    This application uses an LSTM neural network to predict the next word based on your input text.
    
    **How it works:**
    1. Enter a sequence of words
    2. The model processes the input
    3. Get the predicted next word
    """)
    
    st.subheader("⚙️ Model Settings")
    num_predictions = st.slider("Number of words to predict ahead", 1, 5, 1)
    temperature = st.slider("Creativity (temperature)", 0.1, 2.0, 1.0, step=0.1)

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📝 Input Text")
    user_input = st.text_input(
        "Enter a sequence of words:",
        placeholder="e.g., 'the quick brown fox'",
        label_visibility="collapsed"
    )

with col2:
    st.subheader("🎯 Settings")
    top_k = st.selectbox("Top-K predictions", [1, 3, 5], index=0)

# Prediction function
def predict_next_word(input_text, model, tokenizer, max_len, num_words=1, temperature=1.0):
    predictions = []
    
    for _ in range(num_words):
        # Tokenize and pad
        token_list = tokenizer.texts_to_sequences([input_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_len-1, padding='pre')
        
        # Predict
        predicted = model.predict(token_list, verbose=0)
        
        # Apply temperature
        predicted = np.log(predicted + 1e-10) / temperature
        predicted = np.exp(predicted) / np.sum(np.exp(predicted))
        
        # Get top predictions
        top_indices = np.argsort(predicted[0])[-top_k:][::-1]
        
        # Sample from top-k
        sampled_idx = np.random.choice(top_indices, p=predicted[0][top_indices] / predicted[0][top_indices].sum())
        
        # Get word
        output_word = tokenizer.sequences_to_texts([[sampled_idx]])[0]
        predictions.append((output_word, predicted[0][sampled_idx]))
        
        # Update input
        input_text += " " + output_word
    
    return predictions, input_text

# Make prediction
if user_input.strip():
    try:
        with st.spinner("🤔 Predicting..."):
            predictions, full_text = predict_next_word(
                user_input, 
                model, 
                tokenizer, 
                max_len,
                num_words=num_predictions,
                temperature=temperature
            )
        
        # Display results
        st.markdown('<div class="prediction-box">', unsafe_allow_html=True)
        st.subheader("✨ Predictions")
        
        for i, (word, confidence) in enumerate(predictions, 1):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**Word {i}:** {word.strip()}")
            with col2:
                st.write(f"**Confidence:** {confidence:.2%}")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Display generated text
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.subheader("📖 Generated Text")
        st.write(f"*{full_text.strip()}*")
        st.markdown('</div>', unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"❌ Error during prediction: {str(e)}")
else:
    st.info("👈 Enter some words to get started!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #999; font-size: 0.9em;">
    <p>Built with Streamlit & TensorFlow</p>
</div>
""", unsafe_allow_html=True)
