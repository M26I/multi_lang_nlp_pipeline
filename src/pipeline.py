from langdetect import detect, DetectorFactory, LangDetectException
from deep_translator import GoogleTranslator, exceptions as gt_exceptions
from nlp_processor import analyze_text  
from advanced_nlp import advanced_ner, advanced_sentiment 

DetectorFactory.seed = 0  # Make langdetect deterministic

def detect_language(text: str) -> str:
    """
    Detects the language of the input text.
    Returns language code (e.g., 'en') or 'unknown' if detection fails.
    """
    try:
        lang = detect(text)
        return lang
    except LangDetectException:
        return "unknown"

def translate_to_english(text: str, source_lang: str = None) -> str:
    """
    Translates text to English using GoogleTranslator.
    If source_lang is not provided, will detect automatically.
    Returns original text on failure.
    """
    try:
        if not source_lang:
            source_lang = detect_language(text)
        if source_lang == "en" or source_lang == "unknown":
            return text
        translated = GoogleTranslator(source=source_lang, target="en").translate(text)
        return translated
    except (gt_exceptions.NotValidPayload, gt_exceptions.NotValidLength, Exception) as e:
        print(f"Translation failed: {e}")
        return text

def detect_and_translate(text: str) -> str:
    """
    Detect language of text and translate to English if needed.
    """
    lang = detect_language(text)
    return translate_to_english(text, source_lang=lang)

def full_analysis(text: str) -> dict:
    """
    Runs full analysis pipeline combining:
    - Basic NLP (tokens, polarity, etc.)
    - Advanced NER
    - Advanced Sentiment analysis
    Returns a dictionary with results.
    """
    basic_results = analyze_text(text)
    ner_results = advanced_ner(text)
    sentiment_results = advanced_sentiment(text)
    return {
        "basic": basic_results,
        "ner": ner_results,
        "sentiment": sentiment_results
    }

if __name__ == "__main__":
    input_text = input("Enter text: ").strip()
    processed_text = detect_and_translate(input_text)
    print(f"\nProcessed Text: {processed_text}\n")

    results = full_analysis(processed_text)

    print("Basic NLP Results:")
    print(f"Tokens: {results['basic'].get('tokens')}")
    print(f"Polarity: {results['basic'].get('polarity')}")
    print(f"Subjectivity: {results['basic'].get('subjectivity')}")
    print(f"Noun Phrases: {results['basic'].get('noun_phrases')}\n")

    print("Advanced NER Results:")
    print(results['ner'])

    print("\nAdvanced Sentiment Results:")
    print(results['sentiment'])
