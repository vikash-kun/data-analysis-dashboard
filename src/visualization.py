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
def plot_content_type_over_time(df):
    movies = df[df["type"] == "Movie"]
    tv_shows = df[df["type"] == "TV Show"]

    movie_counts = movies["release_year"].value_counts().sort_index()
    tv_counts = tv_shows["release_year"].value_counts().sort_index()

    plt.figure(figsize=(12, 6))

    plt.plot(movie_counts.index, movie_counts.values, label="Movies")
    plt.plot(tv_counts.index, tv_counts.values, label="TV Shows")

    plt.title("Movies vs TV Shows by Release Year")
    plt.xlabel("Release Year")
    plt.ylabel("Number of Titles")

    plt.legend()
    plt.tight_layout()
    plt.show()
def plot_ratings(df):
    ratings = df["rating"].value_counts().head(10)

    plt.figure(figsize=(10, 6))

    plt.bar(ratings.index, ratings.values)

    plt.title("Top 10 Netflix Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Number of Titles")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()   

def plot_top_genres(df, n=10):
    genres = df["listed_in"].str.split(", ").explode()

    genre_counts = genres.value_counts().head(n)

    plt.figure(figsize=(10, 6))

    genre_counts.sort_values().plot(kind="barh")

    plt.title(f"Top {n} Netflix Genres")
    plt.xlabel("Number of Titles")
    plt.ylabel("Genre")

    plt.tight_layout()

    plt.savefig("top_genres.png")
    plt.close()

    print("Top genres chart saved as top_genres.png")     