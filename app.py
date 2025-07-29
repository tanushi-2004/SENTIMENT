# app.py

import streamlit as st
import nlp_processor  # Imports your NLP code

# --- Page Configuration ---
# Sets the title that appears in the browser tab
st.set_page_config(page_title="S.A.M. Journal", layout="centered")

# --- Main Application UI ---
st.title("S.A.M. - Sentient Analysis & Memory Journal")

st.header("New Journal Entry")

# Creates a large text area for the user to write in
entry_text = st.text_area("How are you feeling today?", height=250, placeholder="Write your thoughts here...")

# Creates the button to trigger the analysis
if st.button("Analyze Entry"):
    # Checks if the user has actually written something
    if entry_text:
        # Shows a "spinner" message while the AI is working
        with st.spinner("Analyzing your thoughts..."):
            emotion_results = nlp_processor.analyze_emotions(entry_text)
        
        st.success("Analysis complete!")
        
        # --- Display Results ---
        st.subheader("Analysis of Your Entry")
        
        # Sort emotions by score to show the most dominant ones first
        sorted_emotions = sorted(emotion_results.items(), key=lambda item: item[1], reverse=True)
        
        # Display the top 5 emotions
        st.write("**Top 5 detected emotions:**")
        for emotion, score in sorted_emotions[:5]:
            st.write(f"- {emotion.capitalize()}: {int(score * 100)}%")
        
        # A dropdown "expander" to show the full JSON results if the user is curious
        with st.expander("Show all emotion scores"):
            st.json(emotion_results)
    else:
        # Shows a warning if the user clicks the button with no text
        st.warning("Please write an entry before analyzing.")