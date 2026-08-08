import pandas as pd


def check_missing_values(df):
    print("===== Missing Values =====")
    print(df.isnull().sum())
def total_missing_values(df):
    print("===== Total missing values =====")
    total_missing = df.isnull().sum().sum()
    print("\nTotal missing values:", total_missing)
def check_duplicates(df):
    print("===== Duplicate rows =====")
    print("Number of duplicate rows:", df.duplicated().sum())  
def show_missing_rows(df, column):
    print(f"===== Missing values in {column} =====")
    print(df[df[column].isnull()][["title", column]].head(10))   
def clean_missing_values(df):
    df["director"] = df["director"].fillna("Unknown")
    df["cast"] = df["cast"].fillna("Unknown")
    df["country"] = df["country"].fillna("Unknown")
    df["date_added"] = df["date_added"].fillna("Unknown")
    df["rating"] = df["rating"].fillna("Unknown")
    df["duration"] = df["duration"].fillna("Unknown")

    return df       