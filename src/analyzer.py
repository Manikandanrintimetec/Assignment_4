from src.text_processor import TextProcessor
from src.regex_analyzer import RegexAnalyzer
from src.pos_analyzer import POSAnalyzer
from src.morphology import MorphologyAnalyzer
from src.semantic import SemanticAnalyzer

class Analyzer:

    def __init__(self):
        self.tp = TextProcessor()
        self.regex = RegexAnalyzer()
        self.pos = POSAnalyzer()
        self.morph = MorphologyAnalyzer()
        self.semantic = SemanticAnalyzer()

    def analyze(self, text):
        clean = self.tp.clean_text(text)

        return {
            "basic": {
                "words": self.tp.word_count(clean),
                "chars": self.tp.char_count(clean),
                "avg_len": self.tp.avg_word_length(clean)
            },
            "regex": self.regex.extract_all(text),
            "pos": self.pos.analyze(clean),
            "morph": self.morph.analyze(clean),
            "semantic": self.semantic.analyze(clean)
        }