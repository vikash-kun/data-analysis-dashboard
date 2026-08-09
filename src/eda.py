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