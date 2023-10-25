import numpy as np
import pandas as pd
import os


path = os.path.join(os.getcwd(),"ratings.csv")

data = pd.read_csv(path)

# print(data.shape)


# option = input("""
#        Select your options:
#        a)Display first raw and count of rating
#        """)

transformedData = data.groupby("userId").apply(lambda x: dict(zip(x['movieId'], x['rating'])))
print(transformedData)



# while True:
#      if option == "a":
        
        