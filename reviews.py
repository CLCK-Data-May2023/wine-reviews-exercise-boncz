# add your code here
import zipfile
import pandas as pd

df_wine_reviews = pd.read_csv('data/winemag-data-130k-v2.csv.zip', compression='zip')

df_wine_by_countries_points = df_wine_reviews.groupby('country').agg({'country':'count', 'points': 'mean'}).round(1)
df_updated = df_wine_by_countries_points.rename(columns={'country':'count'}).reset_index()
df_updated.to_csv('data/reviews-per-country.csv', index=False)
