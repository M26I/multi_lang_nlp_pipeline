# © 2025 M26I - For educational/portfolio use only
from textblob import TextBlob

def analyze_text(text):
    blob = TextBlob(text)
    
    tokens = blob.words
    sentiment = blob.sentiment
    noun_phrases = blob.noun_phrases
    
    return {
        "tokens": tokens,
        "polarity": sentiment.polarity,       # -1 to 1 (negative to positive)
        "subjectivity": sentiment.subjectivity,  # 0 to 1 (objective to subjective)
        "noun_phrases": noun_phrases
    }

if __name__ == "__main__":
    sample = input("Enter text for NLP analysis: ")
    results = analyze_text(sample)
    print(f"Tokens: {results['tokens']}")
    print(f"Polarity: {results['polarity']}")
    print(f"Subjectivity: {results['subjectivity']}")
    print(f"Noun Phrases: {results['noun_phrases']}")
