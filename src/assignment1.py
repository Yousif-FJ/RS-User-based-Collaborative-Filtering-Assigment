import pandas as pd
import os
from tools.correlation import *
from tools.prediction import *

path = os.path.join(os.getcwd(), "ratings.csv")
data = pd.read_csv(path)

print('Showing the top rows')
print(data.head())
print( f'Number of ratings in the dataset {data.shape[0]}')


# removing the timestamp because it is unnecessary
data = data[['userId','movieId','rating']]

# reshape the data to be group by userId and create column for each movieId with rating in it
reshapedData = data.pivot(index='userId', columns='movieId', values='rating')

# select one user rating to compare again the rest of the data
targetUserId = 1

# get the target user ratings
targetUserRatings = reshapedData.loc[targetUserId]

# Find similar users to the target user
similarUsersCorrelation = CalculateSimilarUsersCorrelations(reshapedData, targetUserRatings)

print(f'Most similar users to the user with Id {targetUserId}')
print(similarUsersCorrelation)

similarUsersRatings = reshapedData.loc[similarUsersCorrelation.index]
 

movieIds = data['movieId'].unique()

bestMoviesForTargetUser = findBestMoviesForUser(similarUsersRatings, targetUserRatings, movieIds)

print(f'Most relevant movies to the user with Id {targetUserId}')
print(bestMoviesForTargetUser)
