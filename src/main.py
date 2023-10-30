import pandas as pd
import os
from correlation import findSimilarUsers
from prediction import predictRating
from util import *


path = os.path.join(os.getcwd(),"ratings.csv")
data = pd.read_csv(path)
# --------------------------------- Answer a
print('Showing the top rows')
print(data.head())
print( f'Number of ratings in the dataset {data.shape[0]}')

# --------------------------------- Answer b

# removing the timestamp because it is unnecessary
data = data[['userId','movieId','rating']]

# reshape the data to be group by userId and create column for each movieId with rating in it
reshapedData = data.pivot(index='userId', columns='movieId', values='rating')

# select one user rating to compare againt the rest of the data
user1Ratings = reshapedData.loc[1]

similarUsersCorrelation = findSimilarUsers(reshapedData, user1Ratings)

similarUsersRatings = reshapedData.loc[similarUsersCorrelation.index]


predictionTargetMovieId = 101
print(predictRating(similarUsersRatings, user1Ratings, predictionTargetMovieId))
# user2MovieRatingSeries = reshapedData.loc[473]
# visualizeTheData(user1Ratings, user2MovieRatingSeries)