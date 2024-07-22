import pandas as pd
import numpy as np

# Load data from csv file
df = pd.read_csv('data.csv')

# Data preprocessing: Imputation on 'lead_time' using Mean
df['lead_time'].fillna(df['lead_time'].mean(), inplace=False)

# Data preprocessing: duplicate values
df.drop_duplicates(inplace=True)

# Data preprocessing: feature deletion for 'sku'
df = df.drop(['sku'], axis=1)

# Save the transformed data frame as cleaned_data.csv
df.to_csv('cleaned_data.csv', index=False)

# Print the top 5 rows of cleaned dataframe
print(df.head())