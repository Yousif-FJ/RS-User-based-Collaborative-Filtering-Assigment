import pandas as pd
from .SimilarityContainer import *
from .correlation import *


def findBestMoviesForGroup(data : pd.DataFrame, userGroupRatings : pd.DataFrame,
                           movieIds) -> pd.Series:
    movieIdWithRating = dict()
    similarityContainer = SimilarityContainer(data)

    for movieId in movieIds:
        skipMovie = False
        ratingSum = 0
        for (userId, userRatings) in userGroupRatings.iterrows():

            similarUsersRatings = similarityContainer.getSimilarUsers(userRatings)

            predictedRating = predictRating(similarUsersRatings, userRatings, movieId)
            if predictedRating == None:
                skipMovie = True
                break

            ratingSum += predictedRating

        if(skipMovie):
            continue

        numberOfUsersInAGroup = userGroupRatings.shape[0]
        movieIdWithRating[movieId] = ratingSum/numberOfUsersInAGroup
    
    movieIdWithRating = pd.Series(movieIdWithRating).sort_values(ascending=False)

    return movieIdWithRating.head(10)



def findBestMoviesForUser(similarUsersRatings : pd.DataFrame, targetUserRatings : pd.Series,
                           movieIds) -> pd.Series:
    movieIdWithRating = dict()

    for movieId in movieIds:
        predictedRating = predictRating(similarUsersRatings, targetUserRatings, movieId)
        if predictedRating == None:
            continue
        movieIdWithRating[movieId] = predictedRating
    
    movieIdWithRating = pd.Series(movieIdWithRating).sort_values(ascending=False)

    return movieIdWithRating.head(10)



def predictRating(similarUsersRating : pd.DataFrame, targetUserRatings : pd.Series, targetMovieId : int) -> float :

    #filter users who don't have rating on the target movie
    similarUsersRating = similarUsersRating[~similarUsersRating[targetMovieId].isna()]

    #no ratings on the target movie for the given similar users
    if len(similarUsersRating) < 1:
        return None

    targetUserRatingsAverage = targetUserRatings.mean()

    numerator = 0
    for userId, ratings in similarUsersRating.iterrows():
        targetMovieRating = ratings.get(targetMovieId)
        IteratingUserRatingsAverage = ratings.mean()
        correlationBetweenUserRatings = CalculateCorrelation(targetUserRatings,ratings)

        if correlationBetweenUserRatings == None:
            continue

        RatingDifference = targetMovieRating - IteratingUserRatingsAverage
        numerator += correlationBetweenUserRatings * RatingDifference
    
    denominator = 0
    for userId, ratings in similarUsersRating.iterrows():
        correlationBetweenUserRatings = CalculateCorrelation(targetUserRatings,ratings)
        if correlationBetweenUserRatings == None:
            continue

        denominator += correlationBetweenUserRatings

    neighborBias = numerator/denominator

    return targetUserRatingsAverage + neighborBias

