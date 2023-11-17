import pandas as pd
from .correlation import *

class SimilarityContainer:
    
    def __init__(self, data : pd.DataFrame):
        self.data = data
        self.userId_SimilarUsersDictionary = dict()


    def getSimilarUsers(self, userRatings : pd.Series):
        similarUsers = self.userId_SimilarUsersDictionary.get(userRatings.name)

        if(similarUsers is None):
            similarUsers = CalculateSimilarUsers(self.data, userRatings)
            self.userId_SimilarUsersDictionary[userRatings.name] = similarUsers
        
        return similarUsers