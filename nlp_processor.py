# nlp_processor.py

from transformers import pipeline
import streamlit as st # We import streamlit here just for its caching feature

# This is the official name of the pre-trained model we're using
MODEL_NAME = "SamLowe/roberta-base-go_emotions"

@st.cache_resource # This is a "decorator" that tells Streamlit to run this function only once
                   # and save the result. This prevents reloading the huge model every time.
def load_model():
    """Loads and caches the NLP model."""
    print("Loading NLP model...") # This will print only the first time you run the app
    classifier = pipeline(
        "text-classification",
        model=MODEL_NAME,
        top_k=None # This tells the model to return scores for all 27 emotions
    )
    print("Model loaded.")
    return classifier

def analyze_emotions(text: str) -> dict:
    """
    Analyzes a string of text and returns a dictionary of emotion scores.
    """
    if not text:
        return {}

    classifier = load_model()
    results = classifier(text)

    # The model returns a nested list, so we format it into a simple dictionary
    emotion_scores = {item['label']: round(item['score'], 4) for item in results[0]}
    return emotion_scores