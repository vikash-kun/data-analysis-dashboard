import pandas as pd
from src.clean_data import (
    check_missing_values,
    total_missing_values,
    check_duplicates,
    show_missing_rows,
    clean_missing_values,
    find_suspicious_ratings,
    fix_rating_duration
)
from src.analysis import explore_data
from src.eda import (
    content_type_count,
    content_type_percentage,
    release_year_range,
    most_common_release_years,
    most_common_ratings,
    compare_content_types,
    compare_release_years,
    most_common_year_by_type,
    rating_analysis,
    top_ratings,
    country_analysis,
    top_countries
)
from src.visualization import (
    plot_content_type,
    plot_release_year_trend,
    plot_content_type_over_time,
    plot_ratings,
    plot_top_genres,
    plot_genres_by_content_type,
    plot_top_countries
)
df = pd.read_csv(r"C:\Users\Vikash\git demo\data-analysis-dashboard\data\netflix_titles.csv")
#explore_data(df)
df = pd.read_csv(r"C:\Users\Vikash\git demo\data-analysis-dashboard\data\netflix_titles.csv")

# Check original data
check_missing_values(df)
total_missing_values(df)
check_duplicates(df)

show_missing_rows(df, "director")
show_missing_rows(df, "cast")
show_missing_rows(df, "country")
show_missing_rows(df, "date_added")
show_missing_rows(df, "rating")
show_missing_rows(df, "duration")

# Day 10: Find suspicious values
find_suspicious_ratings(df)

# Day 11: Fix misplaced duration values
df = fix_rating_duration(df)

# Then clean the remaining missing values
df = clean_missing_values(df)

print("\n===== Missing Values After Cleaning =====")
print(df.isnull().sum())

# Analysis AFTER cleaning
content_type_count(df)
content_type_percentage(df)
release_year_range(df)
most_common_release_years(df)
most_common_ratings(df)

compare_content_types(df)
compare_release_years(df)
most_common_year_by_type(df)

rating_analysis(df)
top_ratings(df)

# Charts
# Charts

plot_content_type(df)
plot_release_year_trend(df)
plot_content_type_over_time(df)
plot_ratings(df)
plot_top_genres(df)
plot_genres_by_content_type(df)
plot_top_countries(df)

rating_analysis(df)
top_ratings(df)

country_analysis(df)
top_countries(df)

import pandas as pd
from src.clean_data import (
    check_missing_values,
    total_missing_values,
    check_duplicates,
    show_missing_rows,
    clean_missing_values,
    find_suspicious_ratings,
    fix_rating_duration
)
from src.analysis import explore_data
from src.eda import (
    content_type_count,
    content_type_percentage,
    release_year_range,
    most_common_release_years,
    most_common_ratings,
    compare_content_types,
    compare_release_years,
    most_common_year_by_type,
    rating_analysis,
    top_ratings,
    country_analysis,
    top_countries,
    country_by_content_type,
    country_genre_analysis
)
from src.visualization import (
    plot_content_type,
    plot_release_year_trend,
    plot_content_type_over_time,
    plot_ratings,
    plot_top_genres,
    plot_genres_by_content_type,
    plot_top_countries,
    plot_countries_by_content_type,
    plot_country_genres
)
df = pd.read_csv(r"C:\Users\Vikash\git demo\data-analysis-dashboard\data\netflix_titles.csv")
#explore_data(df)
df = pd.read_csv(r"C:\Users\Vikash\git demo\data-analysis-dashboard\data\netflix_titles.csv")

# Check original data
check_missing_values(df)
total_missing_values(df)
check_duplicates(df)

show_missing_rows(df, "director")
show_missing_rows(df, "cast")
show_missing_rows(df, "country")
show_missing_rows(df, "date_added")
show_missing_rows(df, "rating")
show_missing_rows(df, "duration")

# Day 10: Find suspicious values
find_suspicious_ratings(df)

# Day 11: Fix misplaced duration values
df = fix_rating_duration(df)

# Then clean the remaining missing values
df = clean_missing_values(df)

print("\n===== Missing Values After Cleaning =====")
print(df.isnull().sum())

# Analysis AFTER cleaning
content_type_count(df)
content_type_percentage(df)
release_year_range(df)
most_common_release_years(df)
most_common_ratings(df)

compare_content_types(df)
compare_release_years(df)
most_common_year_by_type(df)

rating_analysis(df)
top_ratings(df)



country_analysis(df)
top_countries(df)
country_by_content_type(df)

country_genre_analysis(df, "India")
country_genre_analysis(df, "United States")
country_genre_analysis(df, "Japan")

# Charts
plot_content_type(df)
plot_release_year_trend(df)
plot_content_type_over_time(df)
plot_ratings(df)
plot_top_genres(df)
plot_countries_by_content_type(df)
plot_country_genres(df, "India")
plot_country_genres(df, "United States")
plot_country_genres(df, "Japan")

