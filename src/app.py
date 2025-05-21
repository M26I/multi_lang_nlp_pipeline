import streamlit as st
from pipeline import detect_and_translate, full_analysis
import os
import pandas as pd

st.set_page_config(page_title="MultiLang NLP Pipeline", layout="centered")
st.title("Multi-Language NLP Pipeline Demo")

# --- Helper functions ---

def sentiment_label(polarity_score):
    if polarity_score > 0.1:
        return "Positive 😊"
    elif polarity_score < -0.1:
        return "Negative 😞"
    else:
        return "Neutral 😐"

def explain_basic_nlp(results):
    return f"""
    - **Tokens:** {results.get('tokens')} (words detected in the text)
    - **Polarity:** {results.get('polarity')} ({sentiment_label(results.get('polarity'))}, sentiment score from -1 negative to +1 positive)
    - **Subjectivity:** {results.get('subjectivity')} (0 = very objective, 1 = very subjective)
    - **Noun Phrases:** {', '.join(results.get('noun_phrases')) if results.get('noun_phrases') else 'None detected'}
    """

def load_sample_text(language_name):
    file_map = {
        "English": "english_sample.txt",
        "Spanish": "spanish_sample.txt",
        "German": "german_sample.txt",
        "French": "french_sample.txt"
    }
    filename = file_map.get(language_name)
    if not filename:
        return ""
    file_path = os.path.join("data", filename)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# --- UI ---

sample_language = st.selectbox(
    "Choose example language (or leave blank to enter your own text):",
    options=["", "English", "Spanish", "German", "French"],
    index=0
)

if sample_language:
    user_input = st.text_area(
        "Input text (editable):",
        value=load_sample_text(sample_language),
        height=150
    )
else:
    user_input = st.text_area("Enter text in any language:", height=150)

if st.button("Analyze") and user_input.strip():
    with st.spinner("Processing..."):
        processed_text = detect_and_translate(user_input)
        results = full_analysis(processed_text)

    st.markdown("### Processed Text (translated to English):")
    st.write(processed_text)

    # Advanced Sentiment Analysis (friendly summary)
    st.markdown("### Advanced Sentiment Analysis:")
    sent = results['sentiment']
    st.write(f"Sentiment: **{sent.get('label', 'N/A')}** with score **{sent.get('score', 0):.2f}**")

    # Basic NLP explained
    st.markdown("### Basic NLP Results Explained:")
    st.markdown(explain_basic_nlp(results['basic']))

    # Advanced Named Entity Recognition (NER) as table
    st.markdown("### Advanced Named Entity Recognition (NER):")
    ner = results['ner']
    if ner:
        df_ner = pd.DataFrame(ner)
        st.table(df_ner)
    else:
        st.write("No named entities detected.")

else:
    st.info("Enter some text or select an example and click 'Analyze' to run the NLP pipeline.")
