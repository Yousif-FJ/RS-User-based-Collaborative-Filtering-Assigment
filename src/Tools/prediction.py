import pandas as pd
from .SimilarityContainer import *
from .correlation import *


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





def predictRating(similarUsersRating : pd.DataFrame, targetUserRatings : pd.Series,
                   targetMovieId : int, getActualValueIfExist = True) -> float :

    if(getActualValueIfExist):
        ratingResult = targetUserRatings.get(targetMovieId)
        if(pd.isna(ratingResult) == False):
            return ratingResult

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

