import pandas as pd
from src.clean_data import check_missing_values, total_missing_values, check_duplicates,show_missing_rows,clean_missing_values
from src.analysis import explore_data

df = pd.read_csv(r"C:\Users\Vikash\git demo\data-analysis-dashboard\data\netflix_titles.csv")
#explore_data(df)

check_missing_values(df)
total_missing_values(df)
check_duplicates(df)
show_missing_rows(df, "director")
show_missing_rows(df, "cast")
show_missing_rows(df, "country")
show_missing_rows(df, "date_added")
show_missing_rows(df, "rating")
show_missing_rows(df, "duration")
df = clean_missing_values(df)

print("\n===== Missing Values After Cleaning =====")
print(df.isnull().sum())
