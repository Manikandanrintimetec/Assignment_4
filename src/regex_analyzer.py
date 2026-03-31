import re

class RegexAnalyzer:

    def extract_all(self, text):
        return {
            "dates": re.findall(r'\d{2}[/-]\d{2}[/-]\d{4}|[A-Za-z]+ \d{1,2}, \d{4}', text),
            "percentages": re.findall(r'\d+%', text),
            "money": re.findall(r'\$\d+(?:\.\d+)?', text),
            "time_phrases": re.findall(r'\b\d+ (?:years?|months?|minutes?)\b', text)
        }