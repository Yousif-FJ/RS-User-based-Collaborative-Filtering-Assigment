### Assignment 3: Sequential Group Recommendation
For this assignment I wil implement my own solution. In short, my method uses mean aggregation in the iterations and tries to compensate the least satisfied user from the previous iteration.


### The algorithm:
The algorithm is as follows:
1) First iteration starts with the normal group mean aggregation and results in one item.
2) Remove the recommended item.
3) Identify the least satisfied user from the previous iteration.
4) Create a weight array where the least satisfied user has weight of 2 while other users have 1.
5) Calculate the mean aggregation with the new weights.
6) Repeat from step 2


### Example:
We will consider a simple example to show how this method logically works. Example code run for this same example can be found in the file `src/sequentialRecommendationExample.py`

Suppose we have the following data, started with group mean aggregation as follows:

|       | item1 | item2 | item3 | item4 | item5 |
|-------|-------|-------|-------|-------|-------|
| user1 | 5     | 4     | 2     | 3     | 1     |
| user2 | 5     | 5     | 4     | 5     | 3     |
| user3 | 2     | 2     | 4     | 1     | 5     |
| mean  | 4     | 3.66  | 3.33  | 3     | 3     |

The recommended item would item1 because it has the highest group rating, and the least satisfied user would be user3 because he has the lowest personal rating for that recommended item. Therefore, the algorithm will compensate him, in the next iteration. The next iteration calculation would be:

|       | item2 | item3 | item4 | item5 |
|-------|-------|-------|-------|-------|
| user1 | 4     | 2     | 3     | 1     |
| user2 | 5     | 4     | 5     | 3     |
| user3 | 2     | 4     | 1     | 5     |
| comps | 2     | 4     | 1     | 5     |
| mean  | 3.25  | 3.5   | 2.5   | 3.5   |

The recommend item will be item3.

We can compare normal group mean aggregation and our method:

Normal  : item1 -> item2 -> item3 -> item4 -> item5
Modified: item1 -> item3 -> item2 -> item5 -> item4

We notice how the algorithm was more in favor of user3, which would have made user3 unsatisfied again.

### Why this method should be good:
The methods tries to make sure that unsatisfied user becomes satisfied. We also see the method modifies the values slightly but not radically, this helps keeps the algorithm recommendation close to the optimal best possible recommendation while being fair for the unsatisfied users.

We note that this method is similar to the group mean aggregation, but the twist is that we duplicate the values of the least satisfied user from the last iteration. The duplication process resembles doing a weighted mean. 

### Inspiration:
The method takes inspiration from the least misery method, but applies in a sequential manner. Then, it modifies the normal group mean aggregation method to be a weighted group mean aggregation, this way it can achieve its goals of compensating the unsatisfied users.


### Assumptions and Information:
- The main code for the method can be found in `src/tools/sequentialGroupPrediction`.
- The implementation depends on previous assignments for prediction, correlation and group recommendation.
- Least satisfied user is the user who would rate the recommended item the lowest out of the group. 
- The class `SimilarityContainer` was used to cache the similar users.


### Movie Lens run
The code for that run can be found in `src/assignment3.py`

Example run were also provided in this folder. The code may take a minute to finish.