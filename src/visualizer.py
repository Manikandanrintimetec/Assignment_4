import matplotlib.pyplot as plt

class Visualizer:

    def plot(self, topics):
        try:
            words = [w for w, _ in topics]
            counts = [c for _, c in topics]

            plt.figure()
            plt.bar(words, counts)

            plt.title("Top Topics")
            plt.xlabel("Words")
            plt.ylabel("Frequency")

            plt.tight_layout()

            plt.show()   # 🔥 MUST HAVE
        except Exception as e:
            print("Plot error:", e)