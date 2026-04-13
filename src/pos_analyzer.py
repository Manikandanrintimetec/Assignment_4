import nltk
from nltk import pos_tag, word_tokenize
from collections import Counter

class POSAnalyzer:

    def analyze(self, text):
        tokens = word_tokenize(text)
        tags = pos_tag(tokens)

        freq = Counter(tag for _, tag in tags)

        grammar = r"""
            NP: {<DT>?<JJ>*<NN>}
            VP: {<VB.*><DT>?<JJ>*<NN>}
        """

        cp = nltk.RegexpParser(grammar)
        tree = cp.parse(tags)

        noun_phrases = []
        verb_phrases = []

        for subtree in tree:
            if hasattr(subtree, 'label'):
                if subtree.label() == 'NP':
                    noun_phrases.append(" ".join(word for word, _ in subtree))
                elif subtree.label() == 'VP':
                    verb_phrases.append(" ".join(word for word, _ in subtree))

        return {
            "pos_freq": dict(freq),
            "noun_phrases": noun_phrases[:5],
            "verb_phrases": verb_phrases[:5]
        }