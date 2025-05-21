from langdetect import detect, DetectorFactory
from deep_translator import GoogleTranslator
from nlp_processor import analyze_text  

DetectorFactory.seed = 0  # Consistency

def detect_language(text):
    try:
        return detect(text)
    except Exception as e:
        return f"Error detecting language: {e}"

def translate_to_english(text, source_lang=None):
    try:
        return GoogleTranslator(source=source_lang or 'auto', target='en').translate(text)
    except Exception as e:
        return f"Error during translation: {e}"

def detect_and_translate(text):
    lang = detect_language(text)
    if lang != 'en':
        print(f"Detected language: {lang}, translating to English...")
        text = translate_to_english(text, source_lang=lang)
    else:
        print("Text is already in English.")
    return text

if __name__ == "__main__":
    input_text = input("Enter text: ")
    processed_text = detect_and_translate(input_text)
    print(f"\nProcessed Text: {processed_text}\n")

    nlp_results = analyze_text(processed_text)

    print("NLP Results:")
    print(f"Tokens: {nlp_results['tokens']}")
    print(f"Polarity: {nlp_results['polarity']}")
    print(f"Subjectivity: {nlp_results['subjectivity']}")
    print(f"Noun Phrases: {nlp_results['noun_phrases']}")
