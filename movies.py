import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the csv data file
netflix_df = pd.read_csv('netflix_data.csv')

# Filtering 90's movies
movies90s = netflix_df[(netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] <= 1999)]

# Movie duration column in 90's movies
movieDuration = movies90s['duration']

# Finding most frequent movie duration in 90's using pandas
Average_movie_duration = pd.Series.mean(movies90s['duration']) 

# Finding the frequent movie duration using histogram
plt.hist(movieDuration, bins = 10 , edgecolor = 'red')
plt.xlabel('Movie Duration')
plt.ylabel('Number of movies')
plt.title('Movie duration histogram')
plt.show()

# Filtering 90's action movies 
actionMovies = movies90s[movies90s['genre'] == 'Action']

#Filtering short action movies with the duration of less than 90 minutes 
short_movie_count = np.sum(actionMovies['duration'] < 90)

print(short_movie_count)