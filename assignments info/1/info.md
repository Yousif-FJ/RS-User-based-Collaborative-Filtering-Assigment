### Assignment 1:
The assignment is for User-based Collaborative Filtering Recommendations.
Here are some things about the implementation:
- We use Pandas to read and manipulate the data.
- We use the pearson correlation equation for finding the similar users. 
- we use the library scipy for the pearson correlation implementation.
- For pearson correlation, we only take into account when 2 users have more than 4 common movies with ratings. This help to improve the reliability of the result.
- We use threshold of 0.7 for correlation to find the similar users.
- We used the following prediction function:
![predictionFunction](markdownResources/predictionFunction.png)
- For finding the find most relevant movies for a user, we will use the first 1000 movies only, because the computation take too long and we already have 10 movies with predicted result of 5.
- Some movie ratings we are unable to make a user preference prediction because not enough similar users in the data set. Those items are skipped when search for relevant movies.


#### Assignment 1 part e:

Jaccard Similarity:

The Jaccard Index is useful for collaborative filtering because it measures the similarity of users based on the intersection and union of the sets of movies they have rated. It's particularly effective when dealing with sparse data where users have rated only a subset of the items.

Set-Based Comparison:
The function jaccard_similarity converts the movie ratings of each user into sets of movies they have rated. The Jaccard Index is then calculated based on the intersection and union of these sets.

Handling Sparse Data:
The Jaccard Index is well-suited for collaborative filtering in scenarios where users may not have rated the same movies. It considers the commonality and diversity of their preferences.

Scalability:
The Jaccard Index is computationally efficient and scales well, making it suitable for large datasets.

Interoperability:
The resulting Jaccard similarity matrix provides an interpretable measure of similarity between users, facilitating an understanding of user relationships in the collaborative filtering process.