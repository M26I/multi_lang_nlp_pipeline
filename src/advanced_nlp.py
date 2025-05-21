from transformers import pipeline

# Load NER pipeline
ner_pipeline = pipeline("ner", grouped_entities=True)

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def advanced_ner(text):
    """
    Runs Named Entity Recognition on text.
    Returns list of entities with their type and confidence.
    """
    try:
        entities = ner_pipeline(text)
        # Format output nicely
        return [
            {
                "entity": ent['entity_group'],
                "word": ent['word'],
                "score": ent['score']
            }
            for ent in entities
        ]
    except Exception as e:
        return f"NER error: {e}"

def advanced_sentiment(text):
    """
    Runs sentiment analysis on text.
    Returns label and score.
    """
    try:
        result = sentiment_pipeline(text)[0]
        return {"label": result['label'], "score": result['score']}
    except Exception as e:
        return f"Sentiment error: {e}"
