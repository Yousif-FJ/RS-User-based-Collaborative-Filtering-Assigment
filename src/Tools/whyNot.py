import pandas as pd
from .SimilarityContainer import *
from tools.groupPrediction import *

"""
Why not explanation for mean aggregation group recommendation
"""
def whyNot(userGroupRatings : pd.DataFrame, similarityContainer : SimilarityContainer, itemId,
            bestGroupRecommendation : pd.Series):

    reasons = []
    rating = predictRatingForGroup(userGroupRatings, similarityContainer, itemId)

    if rating is not None : 
        reasons.append(f"The group predicted rating is {rating}.")
        betterItemsCount = 0
        for (itemIdRec, ratingRec) in bestGroupRecommendation.items():
            if (ratingRec > rating):
                betterItemsCount += 1
        if betterItemsCount > 0 :
            reasons.append(f"There (is)are {betterItemsCount} item(s) with good/better group ratings in the best items results.")
    else:
        rating = 2.5


    lowPredictedRatingUsers = []
    for (memberUserId, userRatings) in userGroupRatings.iterrows():
        similarUsersRatings = similarityContainer.getSimilarUsers(userRatings)
        memberMovieRating = userRatings.get(itemId)
        if (pd.isna(memberMovieRating)):
            memberMovieRating = predictRating(similarUsersRatings, userRatings, itemId)
            if(memberMovieRating is None):
                reasons.append(f"Similar users to user {memberUserId} did not reviews this item.")
            else:
                if (memberMovieRating < rating):
                    reasons.append(f"Group member {memberUserId} had lower predicted rating of {memberMovieRating} for the item.")
                    lowPredictedRatingUsers.append((memberUserId, userRatings))

        elif (memberMovieRating < rating):
            reasons.append(f"Group member {memberUserId} had lower rating of {memberMovieRating} for the item.")


    lowRatingPeersCount = 0 
    for (memberUserId, userRating) in lowPredictedRatingUsers:
        similarUsers = similarityContainer.getSimilarUsers(userRating)
        for (userId, similarUserRating) in similarUsers.iterrows():
            itemRating = similarUserRating.get(itemId)
            if(pd.isna(itemRating)):
                continue
            elif (itemRating < rating):
                lowRatingPeersCount += 1

    if(lowRatingPeersCount > 0):
        reasons.append(f"{lowRatingPeersCount} of the similar user to the Group members have lower rating for this item")


    return reasons