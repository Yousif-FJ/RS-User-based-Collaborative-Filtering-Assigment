import pandas as pd
from .SimilarityContainer import *
from .correlation import *
from .prediction import *


def findBestMoviesForGroupBorda(userGroupRatings : pd.DataFrame,
                            similarityContainer : SimilarityContainer, movieIds):
    
    # Collect the ratings of each user in the group for each movie in the dataset
    users_MovieIdsRatings = dict()
    for (userId, userRatings) in userGroupRatings.iterrows():
        movieIdsRatings = dict()
        for movieId in movieIds:
            similarUsersRatings = similarityContainer.getSimilarUsers(userRatings)
            predictedRating = predictRating(similarUsersRatings, userRatings, movieId)
            # If we do not have enough data, put an average rating
            if predictedRating == None:
                predictedRating = 2.5
            movieIdsRatings[movieId] = predictedRating

        # Create a series so we can have order for the elements
        movieIdsRatings = pd.Series(movieIdsRatings).sort_values()
        # Rank them based on their order
        movieIdsRank = movieIdsRatings.rank(method='first')
        users_MovieIdsRatings[userId] = movieIdsRank
        

    # Sum up the ranking for each movie for every group member
    movieIdsGroupRank = dict()
    for movieId in movieIds:
        movieGroupRank = 0
        for (userId, userRatings) in userGroupRatings.iterrows():
            movieGroupRank += users_MovieIdsRatings[userId][movieId]
        movieIdsGroupRank[movieId] = movieGroupRank

    movieIdsGroupRank = pd.Series(movieIdsGroupRank).sort_values(ascending=False)

    return movieIdsGroupRank.head(10)
