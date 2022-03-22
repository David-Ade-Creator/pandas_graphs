import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import movies dataset from csv and convert to a pandas dataframe
movies = pd.read_csv("MovieReview.csv")

# Check counts of ratings gotten per year , and also the average ratings for each year
years_dataframe = movies.groupby('Year')["Rating"].agg([np.mean, np.count_nonzero])
years_dataframe = years_dataframe.reset_index()
plt.figure()
# first subplot, Average ratings
plt.subplot(2, 2, 1)
plt.scatter(years_dataframe['Year'], years_dataframe['mean'], label="Average stars")
plt.xlabel("Year")
plt.ylabel("Average rating")
plt.legend()
# second subplot, rating counts per year
plt.subplot(2, 2, 2)
plt.scatter(years_dataframe['Year'], years_dataframe['count_nonzero'], label="Rating counts")
plt.xlabel("Year")
plt.ylabel("Counts per year")
plt.legend()
plt.show()

# Check most watched movies
top_movies = movies.groupby('Movie')['Rating'].agg([np.count_nonzero, np.mean]).sort_values(by="count_nonzero",
                                                                                            ascending=False)

# plot a piechart to understand what genre of movie the audience watch and give better ratings
genres_dataframe = movies.groupby('Genres')['Rating'].mean().reset_index()
genres_name = genres_dataframe['Genres']
rating = genres_dataframe['Rating']
plt.figure()
plt.title("Average rating per genres")
plt.pie(rating, labels=genres_name)
plt.show()

# plot a graph to understand why 2021 had a large amount of viewers but low average rating
movies_2021 = movies[movies['Year'] == 2021]
ratings_2021 = movies_2021.groupby('Rating')['Movie'].count().reset_index()

# compare counts for each rating
plt.title("Counts per ratings for year 2021")
plt.bar(ratings_2021['Rating'], ratings_2021['Movie'], label="Rating counts")
plt.xlabel("Rating")
plt.ylabel("Counts")
plt.legend()
plt.show()
