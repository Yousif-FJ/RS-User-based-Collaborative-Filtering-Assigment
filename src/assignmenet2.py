import pandas as pd
import os
from tools.correlation import *
from tools.prediction import *

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

result = findBestMoviesForGroup(reshapedData, group, movieIds)
print(result)



