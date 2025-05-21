# © 2025 M26I - For educational/portfolio use only
from deep_translator import GoogleTranslator

def translate_to_english(text, source_lang=None):
    try:
        # If source_lang is None, GoogleTranslator auto-detects
        translated = GoogleTranslator(source=source_lang or 'auto', target='en').translate(text)
        return translated
    except Exception as e:
        return f"Error during translation: {e}"

if __name__ == "__main__":
    sample_text = input("Enter text to translate: ")
    translated_text = translate_to_english(sample_text)
    print(f"Translated Text: {translated_text}")
