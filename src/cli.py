# © 2025 M26I - For educational/portfolio use only
import argparse
from pipeline import detect_and_translate
from nlp_processor import analyze_text
import os

def process_text(text):
    processed_text = detect_and_translate(text)
    nlp_results = analyze_text(processed_text)
    return processed_text, nlp_results

def main():
    parser = argparse.ArgumentParser(
        description="Multi-language NLP Pipeline CLI: detect, translate & analyze text"
    )
    parser.add_argument(
        "-t", "--texts", nargs='*', help="Input texts to process", required=False
    )
    parser.add_argument(
        "-f", "--files", nargs='*', help="Paths to text files to process", required=False
    )
    parser.add_argument(
        "-o", "--output", type=str, help="Output file (JSON) to save results", required=False
    )
    
    args = parser.parse_args()

    inputs = []

    if args.texts:
        inputs.extend(args.texts)
    
    if args.files:
        for filepath in args.files:
            if os.path.isfile(filepath):
                with open(filepath, "r", encoding="utf-8") as f:
                    inputs.append(f.read())
            else:
                print(f"File not found: {filepath}")

    if not inputs:
        text = input("Enter text: ")
        inputs.append(text)

    results = []

    for i, text in enumerate(inputs, 1):
        print(f"\n--- Processing input #{i} ---")
        processed_text, nlp_results = process_text(text)
        print(f"Processed Text:\n{processed_text}\n")
        print("NLP Results:")
        print(f"Tokens: {nlp_results['tokens']}")
        print(f"Polarity: {nlp_results['polarity']}")
        print(f"Subjectivity: {nlp_results['subjectivity']}")
        print(f"Noun Phrases: {nlp_results['noun_phrases']}")
        results.append({
            "original_text": text,
            "processed_text": processed_text,
            "nlp": nlp_results
        })

    if args.output:
        import json
        try:
            with open(args.output, "w", encoding="utf-8") as out_file:
                json.dump(results, out_file, ensure_ascii=False, indent=4)
            print(f"\nResults saved to {args.output}")
        except Exception as e:
            print(f"Error saving output file: {e}")

if __name__ == "__main__":
    main()
