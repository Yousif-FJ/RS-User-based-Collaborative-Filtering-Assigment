## Recommender System 
Repository for assignments for [Recommender system course in Tampere university](https://www.tuni.fi/en/students-guide/curriculum/course-units/uta-ykoodi-53272?year=2023).
The assignments are an implementation for certain method for recommender system. 
The assignment and sample runs were included in assignments info folder.

#### How To Run:
Run the assignmentX.py file. Ex:

    python assignment1.py

The Python code expect the following installed global packages:
- pandas
- sciPy

### Assignment 1:
The assignment is for User-based Collaborative Filtering Recommendations.
Here are some things about the implementation:
- We use Pandas to read and manipulate the data.
- We use the pearson correlation equation for finding the similar users. 
- we use the library scipy for the pearson correlation implementation.
- For pearson correlation, we only take into account when 2 users have more than 4 common movies with ratings. This help to improve the reliability of the result and make them more sortable.
- We use threshold of 0.7 for correlation to find the similar users.
- We used the following prediction function:
![predictionFunction](markdownResources\predictionFunction.png)
- For finding the find most relevant M=movies for a user, we will the first 1000 movies only, be computation take too long and we already have 10 movies with predicted result of 5.
- Some movie ratings we are unable to make a user preference prediction because not enough similar users in the data set.

#### Sample run

python .\assignment1.py
Showing the top rows
   userId  movieId  rating  timestamp
0       1        1     4.0  964982703
1       1        3     4.0  964981247
2       1        6     4.0  964982224
3       1       47     5.0  964983815
4       1       50     5.0  964982931
Number of ratings in the dataset 100836
ConstantInputWarning: An input array is constant; the correlation coefficient is not defined.
  warnings.warn(stats.ConstantInputWarning(msg))
Most similar users to the user with Id 1
473    0.962250
511    0.925820
9      0.918559
13     0.878310
366    0.872872
401    0.866921
535    0.866400
90     0.821584
157    0.801784
139    0.790569
476    0.786936
487    0.774597
210    0.767649
114    0.759257
530    0.755929
49     0.750000
162    0.708333
297    0.706281
207    0.701646
dtype: float64
Most relevant movies to the user with Id 1
58      5.0
1057    5.0
52      5.0
818     5.0
25      5.0
2599    5.0
319     5.0
923     5.0
17      5.0
6       5.0
dtype: float64
