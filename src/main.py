import numpy as np
import pandas as pd
import os


path = os.path.join(os.getcwd(),"ratings.csv")

data = pd.read_csv(path)

print('Showing the top rows')
print(data.head())
print()


print( f'Number of ratings in the dataset {data.shape[0]}')


#removing the timestamp because it is unnecessary
data = data[['userId','movieId','rating']]

#reshape the data to be group by userId and create column for each movieId with rating in it
reshapedData = data.pivot(index='userId', columns='movieId', values='rating')

print(reshapedData.head())



# while True:
#      if option == "a":
        
        