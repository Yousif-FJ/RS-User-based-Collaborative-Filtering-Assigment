import pandas as pd
from .SimilarityContainer import *
from .correlation import *
from .prediction import *
from enum import Enum

class GroupAggregationMethod(Enum):
    Mean = 1
    Min = 2


def findBestMoviesForGroup(userGroupRatings : pd.DataFrame,
                            similarityContainer : SimilarityContainer,
                            movieIds, aggregationMethod : GroupAggregationMethod
                            ) -> pd.Series:
    movieIdWithRating = dict()

    for movieId in movieIds:
        movieRatings = []
        for (userId, userRatings) in userGroupRatings.iterrows():

            similarUsersRatings = similarityContainer.getSimilarUsers(userRatings)

            predictedRating = predictRating(similarUsersRatings, userRatings, movieId)
            if predictedRating == None:
                predictedRating = 2.5
            movieRatings.append(predictedRating)


        if(aggregationMethod == GroupAggregationMethod.Mean):
            movieIdWithRating[movieId] =  sum(movieRatings)/len(movieRatings)
        else :
            movieIdWithRating[movieId] =  min(movieRatings)
    
    movieIdWithRating = pd.Series(movieIdWithRating).sort_values(ascending=False)

    return movieIdWithRating.head(10)
