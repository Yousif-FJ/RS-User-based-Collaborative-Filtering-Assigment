### Assignment 2: Group Recommendation
Here are some things about the implementation:
- We use Pandas to read and manipulate the data.
- We use the pearson correlation equation for finding the similar users. 
- we use the library scipy for the pearson correlation implementation.
- For pearson correlation, we only take into account when 2 users have more than 4 common movies with ratings. This help to improve the reliability of the result.
- We use threshold of 0.7 for correlation to find the similar users.
- We use same prediction in assignment 1
- A lot of the code is shared with assignment 1

#### Assignment 2 part b:
For solution that take into account the disagreement we will use the borda count method.

Each item in the ranking is assigned a score depending on its position in
the ranking: the higher the rank, the larger the score is

#### Note:
A class called similarity container was implemented which act as cache for user similarity. 
It saves the results so that it can be reused when trying to predict ratings for movies.