import pandas as pd
from tools.whyNot import *
from tools.groupPrediction import *
from tools.prediction import *


data = {
    'item1': [5, 5, None, None, 4],
    'item2': [4, None, 2, 3, 4],
    'item3': [None, 4, 4, 2, 1],
    'item4': [2, 5, 1, 1, 2],
    'item5': [None, None, 5, 5, 1],
    'item6': [4, None, 2, 3, 5],
    'item7': [None, 5 , 3, None, 4]
}

data = pd.DataFrame(data, index=['user1', 'user2', 'user3', 'user4', 'user5'])
movieIds = data.columns.tolist()

group = data.head(2)

print(data)

similarityContainer = SimilarityContainer(data)

result = findBestMoviesForGroup(group, similarityContainer, movieIds, GroupAggregationMethod.Mean)
print(result)

reasons = whyNot(group, similarityContainer, 'item5', result)

print(reasons)