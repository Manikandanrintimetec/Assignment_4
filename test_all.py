from src.text_processor import TextProcessor

tp = TextProcessor()

assert tp.word_count("hello world") == 2
assert tp.char_count("hello") == 5

print("All tests passed ")

import matplotlib.pyplot as plt

plt.plot([1,2,3], [4,5,6])
plt.show()