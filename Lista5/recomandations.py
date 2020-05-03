import pandas as pd
import numpy as np 

data = pd.read_csv("ml-latest-small/ratings.csv")
data_arr = data[['userId', 'movieId', 'rating']].to_numpy()

uID = np.fromiter([el[0] for el in data_arr if el[1] < 10000], int)
movieID = np.fromiter([el[1] for el in data_arr if el[1] < 10000], int)
rating = np.fromiter([el[2] for el in data_arr if el[1] < 10000], float)

users_ratings = np.vstack((uID, movieID, rating)).T

users = list(set(uID))
movies = list(set(movieID))
users_dict = {el:users.index(el) for el in users}
movies_dict = {el:movies.index(el) for el in movies}

user_movie_rating = np.zeros((len(users), len(movies)))

# user_movie_rating = [userID | movie1 | movie2 | ..]
for user, movie, rate in users_ratings:
    user_movie_rating[users_dict[user], movies_dict[movie]] = rate

