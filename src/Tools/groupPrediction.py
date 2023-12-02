import pandas as pd
from .SimilarityContainer import *
from .correlation import *
from .prediction import *
from enum import Enum
import numpy as np

class GroupAggregationMethod(Enum):
    Mean = 1
    Min = 2

def findBestMoviesForGroup(userGroupRatings : pd.DataFrame,
                            similarityContainer : SimilarityContainer,
                            movieIds, aggregationMethod : GroupAggregationMethod,
                            meanWeights : [] = None) -> pd.Series:
    movieIdWithRating = dict()

    for movieId in movieIds:
        movieRatings = []
        for (userId, userRatings) in userGroupRatings.iterrows():

            similarUsersRatings = similarityContainer.getSimilarUsers(userRatings)
            
            movieRating = predictRating(similarUsersRatings, userRatings, movieId)

            if movieRating is None:
                movieRating = 2.5
            movieRatings.append(movieRating)


        if(aggregationMethod == GroupAggregationMethod.Mean):
            movieIdWithRating[movieId] =  np.average(movieRatings, weights= meanWeights)
        else :
            movieIdWithRating[movieId] =  min(movieRatings)
    
    movieIdWithRating = pd.Series(movieIdWithRating).sort_values(ascending=False)

    return movieIdWithRating.head(10)


def predictRatingForGroup(userGroupRatings : pd.DataFrame,
                            similarityContainer : SimilarityContainer, movieId) -> float:
    
    movieRatings = []
    for (userId, userRatings) in userGroupRatings.iterrows():

        similarUsersRatings = similarityContainer.getSimilarUsers(userRatings)
        
        movieRating = predictRating(similarUsersRatings, userRatings, movieId)

        if movieRating is None:
            break
        movieRatings.append(movieRating)

    if(len(movieRatings) < userGroupRatings.shape[0]) :
        return None

    return np.average(movieRatings)
