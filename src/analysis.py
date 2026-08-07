import pandas as pd

def explore_data(df):
    print("===== First 5 Rows =====")
    print(df.head())

    print("\n===== Last 5 Rows =====")
    print(df.tail())

    print("\n===== Dataset Shape =====")
    print(df.shape)

    print("\n===== Column Names =====")
    print(df.columns)

    print("\n===== Dataset Information =====")
    print(df.info())

    print("\n===== Statistical Summary =====")
    print(df.describe())