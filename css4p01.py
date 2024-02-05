# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:59:40 2024

@author: toriw
"""

import pandas

file = pandas.read_excel("movie_dataset.xlsx")
print(file)
print(file.info())

import pandas as pd
file_path = 'movie_dataset.xlsx'
df = pd.read_excel(file_path)
fill_value = 0 
df.fillna(fill_value, inplace=True)
df.to_excel(file_path, index=False)
target_column = 'Revenue (Millions)'
column_average = df[target_column].mean()

start_year = 2015
end_year = 2017
filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]
total_revenue = filtered_df['Revenue (Millions)'].sum()
column_average1 = filtered_df['Revenue (Millions)'].mean()

most_sells = 2016
movies_in_target_year = df[df['Year'] == most_sells]
movie_count_in_target_year = movies_in_target_year.shape[0]

target_director = 'Christopher Nolan'
movies_by_director = df[df['Director'] == target_director]
movie_count_by_director = movies_by_director.shape[0]

min_rating = 8.0
highly_rated_movies = df[df['Rating'] >= min_rating]
count_highly_rated_movies = highly_rated_movies.shape[0]

median_rating_by_director = movies_by_director['Rating'].median()

average_rating_by_year = df.groupby('Year')['Rating'].mean()
year_highest_average_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()

movies_2006 = df[df['Year'] == 2006]
movies_2016 = df[df['Year'] == 2016]
count_2006 = movies_2006.shape[0]
count_2016 = movies_2016.shape[0]
percentage_increase = ((count_2016 - count_2006) / count_2006) * 100

actors_df = df['Actors'].str.split(',').explode()
most_common_actor = actors_df.value_counts().idxmax()
movies_count_for_most_common_actor = actors_df.value_counts().max()

genres_df = df['Genre'].str.split(',').explode()
unique_genres_count = genres_df.nunique()
unique_genres_list = genres_df.unique()

numerical_df = df.select_dtypes(include='number')
correlation_matrix = numerical_df.corr()
print("Correlation Matrix:")
print(correlation_matrix)

all_actors = df['Actors'].str.split(', ').explode()
most_common_actor = all_actors.mode().iloc[0]
count_most_common_actor = all_actors.value_counts().iloc[0]




