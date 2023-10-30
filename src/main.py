import pandas as pd
import os
from correlation import findSimilarUsers
from util import *


path = os.path.join(os.getcwd(),"ratings.csv")
data = pd.read_csv(path)
# --------------------------------- Answer a
# print('Showing the top rows')
# print(data.head())
# print()

# print( f'Number of ratings in the dataset {data.shape[0]}')


# --------------------------------- Answer b

# removing the timestamp because it is unnecessary
data = data[['userId','movieId','rating']]

# reshape the data to be group by userId and create column for each movieId with rating in it
reshapedData = data.pivot(index='userId', columns='movieId', values='rating')

# select one user rating to compare againt the rest of the data
user1Ratings = reshapedData.loc[1]

similarUserRating = findSimilarUsers(reshapedData, user1Ratings)

print(similarUserRating)

user2MovieRatingSeries = reshapedData.loc[473]
visualizeTheData(user1Ratings, user2MovieRatingSeries)