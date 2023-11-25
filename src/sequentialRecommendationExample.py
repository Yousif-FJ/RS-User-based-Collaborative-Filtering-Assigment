import pandas as pd
from tools.groupPrediction import *
from tools.sequentialGroupPrediction import findBestMoviesForGroupSequentially
from tools.prediction import *


data = {
    'item1': [5, 5, 2],
    'item2': [4, 5, 2],
    'item3': [2, 4, 4],
    'item4': [3, 5, 1],
    'item5': [1, 3, 5]
}

data = pd.DataFrame(data, index=['user1', 'user2', 'user3'])

similarityContainer = SimilarityContainer(data)


print(data)

result = findBestMoviesForGroupSequentially(data.head(3), similarityContainer, data.columns.tolist(),5)
print(result)

result = findBestMoviesForGroup(data.head(3), similarityContainer, data.columns.tolist(),
                                 GroupAggregationMethod.Mean)
print(result)