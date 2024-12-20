import streamlit as st
import pandas as pd
import pickle
from utils.preprocessing import preprocess_text

# Load the pre-trained model and vectorizer
@st.cache_resource
def load_model_and_vectorizer():
    with open(r"models/spam_classifier.pkl", "rb") as model_file:
        classifier = pickle.load(model_file)
    with open(r"models/vectorizer.pkl", "rb") as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    return classifier, vectorizer

classifier, vectorizer = load_model_and_vectorizer()

# Streamlit App
st.title("SMS Spam Classifier")
st.write("A simple application to classify SMS messages as spam or not spam.")

# Input Text
user_input = st.text_area("Enter the SMS text:", placeholder="Type your message here...")

# Prediction Button
if st.button("Predict"):
    if user_input.strip():
        # Preprocess and vectorize input
        processed_text = preprocess_text(user_input)
        vectorized_text = vectorizer.transform([processed_text])
        
        # Make prediction
        prediction = classifier.predict(vectorized_text)
        prediction_label = "Spam" if prediction[0] == 1 else "Not Spam"
        
        # Display Result
        st.subheader("Prediction:")
        st.success(f"The message is classified as **{prediction_label}**.")
    else:
        st.warning("Please enter some text to classify.")

# Footer
st.write("Developed with ❤️ using Streamlit")
