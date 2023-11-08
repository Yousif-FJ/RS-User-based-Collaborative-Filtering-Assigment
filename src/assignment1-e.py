import pandas as pd
import numpy as np
import os

def jaccard_similarity(user1, user2, user_movie_ratings):
    movies_user1 = set(user_movie_ratings.columns[user_movie_ratings.loc[user1] > 0])
    movies_user2 = set(user_movie_ratings.columns[user_movie_ratings.loc[user2] > 0])

    intersection = len(movies_user1.intersection(movies_user2))
    union = len(movies_user1.union(movies_user2))

    if union == 0:
        return 0.0
    else:
        return intersection / union

path = os.path.join(os.getcwd(), "ratings.csv")
data = pd.read_csv(path)


# removing the timestamp because it is unnecessary
data = data[['userId','movieId','rating']]

# reshape the data to be group by userId and create column for each movieId with rating in it
user_movie_ratings = data.pivot(index='userId', columns='movieId', values='rating')
user_movie_ratings = user_movie_ratings.replace(np.nan, 0)

ratings = data.pivot_table(index=f'userId', columns='movieId', values='rating')
# np.nanmean only gets the values and excluded NaN
user_movie_ratings['average_rating'] = np.nanmean(ratings, axis=1)


# Calculate the Jaccard similarity matrix
users_sim_jaccard = pd.DataFrame(index=user_movie_ratings.index, columns=user_movie_ratings.index)
for user1 in user_movie_ratings.index:
    for user2 in user_movie_ratings.index:
        users_sim_jaccard.loc[user1, user2] = jaccard_similarity(user1, user2, user_movie_ratings)

np.fill_diagonal(users_sim_jaccard.values, 0)

# Continue with the rest of your existing code for predictions...

# Example: Print the Jaccard similarity matrix for the first few users
print("Jaccard Similarity Matrix:")
print(users_sim_jaccard.head())
