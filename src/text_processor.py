import re

class TextProcessor:

    def clean_text(self, text):
        try:
            text = text.replace("“", '"').replace("”", '"').replace("’", "'")
            text = re.sub(r'[^a-zA-Z0-9\s.,?]', '', text)
            text = re.sub(r'\s+', ' ', text)
            return text.strip()
        except Exception:
            return ""

    def word_count(self, text):
        return len(text.split())

    def char_count(self, text):
        return len(text)

    def avg_word_length(self, text):
        words = text.split()
        return sum(len(w) for w in words)/len(words) if words else 0