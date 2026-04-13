from nltk.stem import WordNetLemmatizer

class MorphologyAnalyzer:

    def __init__(self):
        self.lem = WordNetLemmatizer()

    def analyze(self, text):
        words = text.split()

        lemmas = [self.lem.lemmatize(w) for w in words]
        compounds = [w for w in words if '-' in w]

        prefixes = [w[:3] for w in words if len(w) > 3]
        suffixes = [w[-3:] for w in words if len(w) > 3]

        return {
            "lemmas": lemmas[:10],
            "compounds": compounds,
            "prefixes": prefixes[:5],
            "suffixes": suffixes[:5]
        }