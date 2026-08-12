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

def plot_release_year_trend(df):
    yearly_counts = df["release_year"].value_counts().sort_index()

    plt.figure(figsize=(12, 6))

    plt.plot(yearly_counts.index, yearly_counts.values)

    plt.title("Netflix Content by Release Year")
    plt.xlabel("Release Year")
    plt.ylabel("Number of Titles")

    plt.tight_layout()
    plt.show()    