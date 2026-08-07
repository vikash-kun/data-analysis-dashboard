import pandas as pd
from src.analysis import explore_data

df = pd.read_csv(r"C:\Users\Vikash\git demo\data-analysis-dashboard\data\netflix_titles.csv")
explore_data(df)