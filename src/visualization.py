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

def plot_genres_by_content_type(df, n=10):
    movie_genres = (
        df[df["type"] == "Movie"]["listed_in"]
        .str.split(", ")
        .explode()
        .value_counts()
        .head(n)
    )

    tv_genres = (
        df[df["type"] == "TV Show"]["listed_in"]
        .str.split(", ")
        .explode()
        .value_counts()
        .head(n)
    )

    fig, axes = plt.subplots(1, 2, figsize=(16, 7))

    movie_genres.sort_values().plot(
        kind="barh",
        ax=axes[0]
    )

    axes[0].set_title("Top Movie Genres")
    axes[0].set_xlabel("Number of Titles")
    axes[0].set_ylabel("Genre")

    tv_genres.sort_values().plot(
        kind="barh",
        ax=axes[1]
    )

    axes[1].set_title("Top TV Show Genres")
    axes[1].set_xlabel("Number of Titles")
    axes[1].set_ylabel("Genre")

    plt.tight_layout()

    plt.savefig("genres_by_content_type.png")
    plt.close()

    print("Genre comparison chart saved as genres_by_content_type.png")
def plot_top_countries(df, n=10):
    countries = df["country"].str.split(", ").explode()

    countries = countries[countries != "Unknown"]

    country_counts = countries.value_counts().head(n)

    plt.figure(figsize=(10, 6))

    country_counts.sort_values().plot(kind="barh")

    plt.title(f"Top {n} Countries by Netflix Titles")
    plt.xlabel("Number of Titles")
    plt.ylabel("Country")

    plt.tight_layout()

    plt.savefig("top_countries.png")
    plt.close()

    print("Top countries chart saved as top_countries.png")
def plot_countries_by_content_type(df, n=10):
    movie_countries = (
        df[df["type"] == "Movie"]["country"]
        .str.split(", ")
        .explode()
    )

    tv_countries = (
        df[df["type"] == "TV Show"]["country"]
        .str.split(", ")
        .explode()
    )

    movie_countries = movie_countries[movie_countries != "Unknown"]
    tv_countries = tv_countries[tv_countries != "Unknown"]

    movie_counts = movie_countries.value_counts().head(n)
    tv_counts = tv_countries.value_counts().head(n)

    fig, axes = plt.subplots(1, 2, figsize=(16, 7))

    movie_counts.sort_values().plot(
        kind="barh",
        ax=axes[0]
    )

    axes[0].set_title("Top Countries for Movies")
    axes[0].set_xlabel("Number of Movies")
    axes[0].set_ylabel("Country")

    tv_counts.sort_values().plot(
        kind="barh",
        ax=axes[1]
    )

    axes[1].set_title("Top Countries for TV Shows")
    axes[1].set_xlabel("Number of TV Shows")
    axes[1].set_ylabel("Country")

    plt.tight_layout()
    plt.savefig("countries_by_content_type.png")
    plt.close()

    print("Country comparison chart saved as countries_by_content_type.png")  

def plot_country_genres(df, country, n=10):
    country_df = df[
        df["country"].str.contains(country, na=False)
    ]

    genres = (
        country_df["listed_in"]
        .str.split(", ")
        .explode()
    )

    genre_counts = genres.value_counts().head(n)

    plt.figure(figsize=(10, 6))

    genre_counts.sort_values().plot(
        kind="barh"
    )

    plt.title(f"Top {n} Genres in {country}")
    plt.xlabel("Number of Titles")
    plt.ylabel("Genre")

    plt.tight_layout()

    filename = f"{country.lower().replace(' ', '_')}_genres.png"

    plt.savefig(filename)
    plt.close()

    print(f"{country} genre chart saved as {filename}")      