import pandas as pd
import os
from correlation import getSimilarUsersCorrelations
from prediction import predictRating
from util import *


path = os.path.join(os.getcwd(), "ratings.csv")
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
targetUserId = 1
predictionTargetMovieId = 101

# get the target user ratings
targetUserRatings = reshapedData.loc[targetUserId]

# Find similar users to the target user
similarUsersCorrelation = getSimilarUsersCorrelations(reshapedData, targetUserRatings)

similarUsersRatings = reshapedData.loc[similarUsersCorrelation.index]
 

print(predictRating(similarUsersRatings, targetUserRatings, predictionTargetMovieId))
