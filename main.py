import sys
from src.analyzer import Analyzer
from src.visualizer import Visualizer
from bs4 import BeautifulSoup
import PyPDF2


def read_file(path):
    try:
        # TXT
        if path.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                return f.read()

        # PDF
        elif path.endswith(".pdf"):
            text = ""
            with open(path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    text += page.extract_text()
            return text

        # HTML
        elif path.endswith(".html"):
            with open(path, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "html.parser")
                return soup.get_text()

    except Exception as e:
        print("Error reading file:", e)
        return ""


def main():
    analyzer = Analyzer()
    visualizer = Visualizer()

    # CLI flags
    detailed = "detail" in sys.argv
    plot = "plot" in sys.argv

    print("\n Processing articles...\n")

    for i in range(1, 11):
        file = f"data/article{i}.txt"
        print(f"\n Processing: {file}")
        print("-" * 50)

        text = read_file(file)

        if not text:
            print("❌ File not found or empty")
            continue

        result = analyzer.analyze(text)

        # BASIC OUTPUT
        print("Word Count:", result["basic"]["words"])
        print("Character Count:", result["basic"]["chars"])
        print("Avg Word Length:", round(result["basic"]["avg_len"], 2))

        print("Top Topics:", result["semantic"]["topics"])

        # DETAILED OUTPUT
        if detailed:
            print("\n--- FULL ANALYSIS ---")
            print("Dates:", result["regex"]["dates"])
            print("POS Frequency:", result["pos"]["pos_freq"])
            print("Noun Phrases:", result["pos"]["noun_phrases"])
            print("Verb Phrases:", result["pos"]["verb_phrases"])
            print("Lemmas:", result["morph"]["lemmas"])
            print("Entities:", result["semantic"]["entities"])
            print("Sentiment:", result["semantic"]["sentiment"])
            print("Complexity:", round(result["semantic"]["complexity"], 2))

        #  PLOT FOR EACH ARTICLE
        if plot:
            visualizer.plot(result["semantic"]["topics"])

    print("\n All articles processed successfully!")


if __name__ == "__main__":
    main()