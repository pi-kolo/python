import pandas as pd
import numpy as np 

data = pd.read_csv("ml-latest-small/ratings.csv")
movies_data = pd.read_csv("ml-latest-small/movies.csv")
data_arr = data[['userId', 'movieId', 'rating']].to_numpy()
movies_names = movies_data[['movieId', "title"]]

uID = np.fromiter([el[0] for el in data_arr if el[1] < 10000], int)
movieID = np.fromiter([el[1] for el in data_arr if el[1] < 10000], int)
rating = np.fromiter([el[2] for el in data_arr if el[1] < 10000], float)
users_ratings = np.vstack((uID, movieID, rating)).T

users = list(set(uID))
movies = list(set(movieID))

#only movies that appears in rating (just to controll indices)
movies_names = movies_names[movies_names['movieId'].isin(movies)].to_numpy()


# movie_id -> index in movies
users_dict = {el:users.index(el) for el in users}
movies_dict = {el:movies.index(el) for el in movies}


# user_movie_rating = [//userID// | movie1 | movie2 | ..]
user_movie_rating = np.zeros((len(users), len(movies)))
for user, movie, rate in users_ratings:
    user_movie_rating[users_dict[user], movies_dict[movie]] = rate

#example data
user_rates = np.zeros((5390, 1))
user_rates[movies_dict[2571]] = 5
user_rates[movies_dict[32]] = 4
user_rates[movies_dict[260]] = 5
user_rates[movies_dict[1097]] = 4

def predict_it(someones_rate):
    normalised = user_movie_rating/np.linalg.norm(user_movie_rating, axis=0)
    z = np.dot(normalised, np.array(someones_rate)/np.linalg.norm(someones_rate))
    z_v = z/np.linalg.norm(z)
    X = normalised
    Z = z_v
    R = np.dot(X.T, Z)
    R2 = [(el[0], i) for i, el in enumerate(R)]
    R2.sort(key = lambda x: x[0])
    result = list(map(lambda x: movies_names[x[1]][1], R2))
    return result[:-20:-1]
