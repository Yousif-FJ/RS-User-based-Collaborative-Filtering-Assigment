import pandas as pd
import os
from tools.groupPrediction import *
from tools.sequentialGroupPrediction import findBestMoviesForGroupSequentially

path = os.path.join(os.getcwd(), "ratings.csv")
data = pd.read_csv(path)

# removing the timestamp because it is unnecessary
data = data[['userId','movieId','rating']]

# reshape the data to be group by userId and create column for each movieId with rating 
reshapedData = data.pivot(index='userId', columns='movieId', values='rating')

movieIds = reshapedData.columns.tolist()

# how should we create a group of users?
# consider group of 3 users
group = reshapedData.head(3)


# use this class to cache similar user, so we don't have to recalculate similar users
similarityContainer = SimilarityContainer(reshapedData)

result = findBestMoviesForGroupSequentially(group, similarityContainer, movieIds)

print(result)
