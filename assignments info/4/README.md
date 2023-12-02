### Assignment 4: Why Not Explanations for recommender system
For this assignment I will use my own algorithm for finding reasons.
My method combine all the types of why not question in one solution and returns an array of explanation.
It is made to assist the developers understand why the system doesn't produce certain results.

The algorithm has 3 phases, it starts from general methods and then tries to be more specific. 
The method has the potential to produce output in every stage in the process.

For a given single item which we are trying to explain:
- Predicting the group rating for the item, and comparing it to the best results.
- Finding the group member that had the lowest predicted rating.
- Counting the lower rating users who are similar to the group members.

#### Code 
The code for this can be found in `src/tools/whyNot.py`. For the assignment MovieLens we find it in `src/assignment4.py`. For the movie lens dataset, we can't predict score for most movies for a group, specific items were chosen for the testing.

Additional example was created in `src/whyNotExample.py`.