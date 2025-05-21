# © 2025 M26I - For educational/portfolio use only

from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0  # ensures consistency

def detect_language(text):
    try:
        lang_code = detect(text)
        return lang_code
    except Exception as e:
        return f"Error detecting language: {e}"

if __name__ == "__main__":
    sample_text = input("Enter text: ")
    detected = detect_language(sample_text)
    print(f"Detected Language Code: {detected}")
