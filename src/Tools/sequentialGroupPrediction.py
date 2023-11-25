import pandas as pd
from .SimilarityContainer import *
from .correlation import *
from .prediction import *
from .groupPrediction import *

def createWeightedAverageArray(size : int, highWeightIndex : int):
    lst = [1]*size
    lst[highWeightIndex] = 2
    return lst


def findLeastSatisfiedUser(userGroupRatings : pd.DataFrame, similarityContainer : SimilarityContainer,
                           movieId : int) -> str:
    
    UserId_RatingDictionary = dict()

    for (userId, userRatings) in userGroupRatings.iterrows():
        similarUsersRatings = similarityContainer.getSimilarUsers(userRatings)
        rating = predictRating(similarUsersRatings, userRatings, movieId)
        UserId_RatingDictionary[userId] = rating

    return min(UserId_RatingDictionary, key=UserId_RatingDictionary.get)


def findBestMoviesForGroupSequentially(userGroupRatings : pd.DataFrame,
                            similarityContainer : SimilarityContainer,
                            movieIds : list, iterationNumber = 3) -> dict:
    result = dict()

    for i in range(1, iterationNumber+1):
        if(i == 1):
            groupRecommendation = findBestMoviesForGroup(userGroupRatings, similarityContainer, movieIds,
                                                          GroupAggregationMethod.Mean).head(1)
        else:
            recommendedMovieIdFromLastIteration = groupRecommendation.first_valid_index()
            unSatisfiedUserId = findLeastSatisfiedUser(userGroupRatings, similarityContainer, 
                                                       recommendedMovieIdFromLastIteration)
            
            indexOfTheUnSatisfiedUser = userGroupRatings.index.tolist().index(unSatisfiedUserId)
            weightArray = createWeightedAverageArray(len(userGroupRatings), indexOfTheUnSatisfiedUser)

            groupRecommendation  = findBestMoviesForGroup(userGroupRatings, similarityContainer, movieIds,
                                                          GroupAggregationMethod.Mean, weightArray).head(1)

        # Remove the item as it has been recommended already
        recommendedMovieId = groupRecommendation.first_valid_index()
        movieIds.remove(recommendedMovieId)
        result[recommendedMovieId] = groupRecommendation.item()

    return result
