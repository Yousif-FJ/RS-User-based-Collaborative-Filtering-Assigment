import pandas as pd

from correlation import CalculateCorrelation


def predictRating(similarUsersRating : pd.DataFrame, targetUserRatings : pd.Series, targetMovieId : int) -> float :

    #filter users who don't have rating on the target movie
    similarUsersRating = similarUsersRating[~similarUsersRating[targetMovieId].isna()]

    #no ratings on the target movie for the given similar users
    if len(similarUsersRating) == 0:
        return None

    numerator = 0
    for userId, ratings in similarUsersRating.iterrows():
        targetMovieRatingForUser = ratings.get(targetMovieId)
        numerator += CalculateCorrelation(ratings, targetUserRatings) * targetMovieRatingForUser
    
    denominator = 0
    for userId, ratings in similarUsersRating.iterrows():
        denominator += CalculateCorrelation(ratings, targetUserRatings)

    return numerator/denominator

