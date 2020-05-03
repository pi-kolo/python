import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv("ml-latest-small/ratings.csv")
data_arr = data[['userId', 'movieId', 'rating']].to_numpy()

#users that watched Toy Story
toy_storied = data_arr[np.where(data_arr[:,1] == 1)]

#cel: [userId | movie1 | movie2 | ...]

uID = np.fromiter([el[0] for el in data_arr if el[0] in toy_storied.T[0]], int)
movieID = np.fromiter([el[1] for el in data_arr if el[0] in toy_storied.T[0]], int)
rating = np.fromiter([el[2] for el in data_arr if el[0] in toy_storied.T[0]], float)

toy_storied_movies = np.vstack((uID, movieID, rating)).T

def get_m_movies_ratings(n, m):
    ratings = np.zeros((n, m))
    for user, movie, rate in toy_storied_movies:
        index = np.where(toy_storied.T[0] == user)[0][0]
        if movie > 1 and movie < m and index < n:
            ratings[np.where(toy_storied.T[0] == user)[0][0], int(movie)-2] = rate
    return ratings

def regression(m_movies, n_users):
    X = get_m_movies_ratings(n_users, m_movies)
    Y = np.reshape(toy_storied.T[2][:n_users], (n_users, 1))
    return LinearRegression().fit(X,Y), X, Y


#lets try to predict next values

ratings = get_m_movies_ratings(215, 10000)
clf, X, Y = regression(10000, 200)
for i in range(200, 215):
    print(f"{clf.predict([ratings[i]])} vs {toy_storied[i][2]}")