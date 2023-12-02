import pandas as pd
import os
from tools.whyNot import *
from tools.groupPrediction import *

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

results = findBestMoviesForGroup(group, similarityContainer, movieIds, GroupAggregationMethod.Mean)
print(results)


sampleMoviesForWhyNot = [1073, 919, 788, 780, 743, 736, 594, 587, 586]
for movieId in sampleMoviesForWhyNot:
    reasons = whyNot(group, similarityContainer, movieId, results)
    reasons.append(f"movie Id {movieId}")
    print(reasons)
