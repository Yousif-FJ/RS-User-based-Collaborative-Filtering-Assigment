import pandas as pd
import os
from tools.groupPrediction import *

path = os.path.join(os.getcwd(), "ratings.csv")
data = pd.read_csv(path)

# removing the timestamp because it is unnecessary
data = data[['userId','movieId','rating']]

# reshape the data to be group by userId and create column for each movieId with rating 
reshapedData = data.pivot(index='userId', columns='movieId', values='rating')

movieIds = data['movieId'].unique()

# how should we create a group of users?
# consider group of 3 users
group = reshapedData.head(3)


# use this class to cache similar user, so we don't have to recalculate similar users
similarityContainer = SimilarityContainer(reshapedData)


print("Calculating best movies for the group using mean aggregation method")
result = findBestMoviesForGroup(group, similarityContainer, movieIds, GroupAggregationMethod.Mean)
print(result)

print("Calculating best movies for the group using min aggregation method")
result = findBestMoviesForGroup(group, similarityContainer, movieIds, GroupAggregationMethod.Min)
print(result)

