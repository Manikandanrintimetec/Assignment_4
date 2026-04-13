from textblob import TextBlob
import spacy
from collections import Counter

class SemanticAnalyzer:

    def __init__(self, lang="en"):
        self.nlp = spacy.load("en_core_web_sm")

    def analyze(self, text):
        blob = TextBlob(text)

        sentiment = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        doc = self.nlp(text)

        entities = [(e.text, e.label_) for e in doc.ents]

        words = [t.text.lower() for t in doc if t.is_alpha]
        topics = Counter(words).most_common(5)

        sentences = len(list(doc.sents))
        complexity = len(words)/sentences if sentences else 0

        return {
            "sentiment": sentiment,
            "subjectivity": subjectivity,
            "entities": entities[:5],
            "topics": topics,
            "complexity": complexity
        }