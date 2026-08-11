import matplotlib.pyplot as plt


def plot_content_type(df):
    counts = df["type"].value_counts()

    plt.figure(figsize=(8, 5))
    plt.bar(counts.index, counts.values)

    plt.title("Netflix Movies vs TV Shows")
    plt.xlabel("Content Type")
    plt.ylabel("Number of Titles")

    plt.tight_layout()
    plt.show()