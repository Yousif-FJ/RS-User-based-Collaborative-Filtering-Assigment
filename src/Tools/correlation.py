from scipy.stats import pearsonr
import pandas as pd
from .util import *


def CalculateCorrelation(userRatings1 : pd.Series, userRatings2 : pd.Series) -> float:        
        # find only the values which are present in both series for the same movie
        (array1, array2) = filterNa(userRatings1, userRatings2)

        # filter to only 4 common movies plus. having less than 4 result in unreliable results
        if(len(array1) < 4) :
            return None

        # correlation = user.corr(user1)
        correlation = pearsonr(array1, array2)[0]
        return correlation


def getSimilarUsersCorrelations(data : pd.DataFrame, userRating : pd.Series) -> pd.Series:

    movieIdWithCorrelation = dict()

    for userId, iteratorUser in data.iterrows():
        # don't compare the user with himself
        if userId == userRating.name:
            continue

        correlation = CalculateCorrelation(iteratorUser, userRating)

        movieIdWithCorrelation[userId] = correlation

    movieIdWithCorrelation = pd.Series(movieIdWithCorrelation).dropna().sort_values(ascending=False)

    return movieIdWithCorrelation.loc[lambda value : value > 0.7]
