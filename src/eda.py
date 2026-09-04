def content_type_count(df):
    print("===== Content Type Count =====")
    print(df["type"].value_counts())
def content_type_percentage(df):
    print("===== Content Type Percentage =====")

    percentage = df["type"].value_counts(normalize=True) * 100

    print(percentage)
def release_year_range(df):
    print("===== Release Year Range =====")

    oldest = df["release_year"].min()
    newest = df["release_year"].max()

    print("Oldest release year:", oldest)
    print("Newest release year:", newest)
def most_common_release_years(df):
    print("===== Most Common Release Years =====")
    print(df["release_year"].value_counts().head(10)) 
def most_common_ratings(df):
    print("===== Most Common Ratings =====")
    print(df["rating"].value_counts().head(10)) 
def compare_content_types(df):
    print("===== Movies vs TV Shows =====")

    movies = df[df["type"] == "Movie"]
    tv_shows = df[df["type"] == "TV Show"]

    print("Movies:", len(movies))
    print("TV Shows:", len(tv_shows))   
def compare_release_years(df):
    print("===== Release Year Comparison =====")

    movies = df[df["type"] == "Movie"]
    tv_shows = df[df["type"] == "TV Show"]

    print("Average Movie release year:", movies["release_year"].mean())
    print("Average TV Show release year:", tv_shows["release_year"].mean())
def most_common_year_by_type(df):
    print("===== Most Common Release Year by Type =====")

    movies = df[df["type"] == "Movie"]
    tv_shows = df[df["type"] == "TV Show"]

    print("\nMovies:")
    print(movies["release_year"].value_counts().head(5))

    print("\nTV Shows:")
    print(tv_shows["release_year"].value_counts().head(5))           
def rating_analysis(df):
    print("===== Rating Analysis =====")

    ratings = df["rating"].value_counts()

    print(ratings)
def top_ratings(df):
    print("===== Top 5 Netflix Ratings =====")

    ratings = df["rating"].value_counts().head(5)

    print(ratings)    

def country_analysis(df):
    print("===== Country Analysis =====")

    print(df["country"].head(10))
def top_countries(df):
    countries = df["country"].str.split(", ")
    
    print(countries.head())
def top_countries(df):
    countries = df["country"].str.split(", ").explode()

    print("===== Top Countries =====")
    print(countries.value_counts().head(10))
def top_countries(df):
    countries = df["country"].str.split(", ").explode()

    countries = countries[countries != "Unknown"]

    print("===== Top 10 Countries =====")
    print(countries.value_counts().head(10)) 
    
def genre_analysis(df):
    print("===== Top 10 Netflix Genres =====")

    genres = df["listed_in"].str.split(", ").explode()

    genre_counts = genres.value_counts()

    print(genre_counts.head(10))           
def genre_by_content_type(df):
    print("===== Top Genres by Content Type =====")

    for content_type in ["Movie", "TV Show"]:
        data = df[df["type"] == content_type]

        genres = data["listed_in"].str.split(", ").explode()

        print(f"\n{content_type}:")
        print(genres.value_counts().head(10)) 
def country_by_content_type(df, n=10):
    movies = (
        df[df["type"] == "Movie"]["country"]
        .str.split(", ")
        .explode()
    )

    tv_shows = (
        df[df["type"] == "TV Show"]["country"]
        .str.split(", ")
        .explode()
    )

    movies = movies[movies != "Unknown"]
    tv_shows = tv_shows[tv_shows != "Unknown"]

    movie_counts = movies.value_counts().head(n)
    tv_counts = tv_shows.value_counts().head(n)

    print("\n===== Top Countries for Movies =====")
    print(movie_counts)

    print("\n===== Top Countries for TV Shows =====")
    print(tv_counts)  
def country_genre_analysis(df, country, n=10):
    country_df = df[
        df["country"].str.contains(country, na=False)
    ]

    genres = (
        country_df["listed_in"]
        .str.split(", ")
        .explode()
    )

    genre_counts = genres.value_counts().head(n)

    print(f"\n===== Top Genres in {country} =====")
    print(genre_counts)

    return genre_counts             