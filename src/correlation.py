from scipy.stats import pearsonr
import pandas as pd
from util import *

def findSimilarUsers(data : pd.DataFrame, userRating : pd.Series) -> pd.Series:
    
    movieIdWithCorrelation = dict()

    for userId, iteratorUser in data.iterrows():
        # don't compare the user with himself
        if userId == userRating.name:
            continue

        # find only the values which are present in both series for the same movie
        (array1, array2) = filterNa(iteratorUser, userRating)

        # filter to only 4 common movies plus. having less than 4 result in unreliable results
        if(len(array1) < 4) :
            continue

        # correaltion = user.corr(user1)
        correaltion = pearsonr(array1, array2)[0]

        movieIdWithCorrelation[userId] = correaltion

    movieIdWithCorrelation = pd.Series(movieIdWithCorrelation).dropna().sort_values(ascending=False)

    return movieIdWithCorrelation.head(10)
