import pandas as pd
import os

# as my root directory for the project is iVedha_assessment therefore I have to iterate over the file
# and run the csv
df = pd.read_csv('Python Code Assignment/assignment data.csv')

# Remove rows where 'sq__ft' or 'price' contains the value 0 or NaN
df = df[(df['sq__ft'] != 0) & (df['price'] != 0) & ~df[['sq__ft', 'price']].isnull().any(axis=1)]
df['price_by_foot'] = df['price']/df['sq__ft'] # created a new column where each element of price is divided by sq__ft

# gets the mean value of that column
mean_score = df['price_by_foot'].mean()

# only keep rows (properties) which has the price_by_foot less that the average
df = df[df['price_by_foot'] < mean_score]

# drops the column price_by_foot
df.drop('price_by_foot', axis=1, inplace=True)

# saves the modified csv to a file named modified_data.csv
output_file = 'Python Code Assignment/modified_data.csv'
df.to_csv(output_file, index=False)