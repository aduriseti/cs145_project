## 11-2-17 report
### Amal
 - took a first pass at sentiment analysis
 - Note the general workflow in the notebook
 	- generate vectors to represent words
 	- aggregate word vectors for each tweet into a single vector for each tweet
 	- train a classifier on tweet vectors
 - was going to annotate w/ comments, but think its easier to explain in person if you don't understand
 #### TODO
 - used word2vec for this pass -- but will also try w/ LDA/LSI/docv2vec as well
 - Also --- will test other classifier models
 - Note also there is no preprocessing - which should improve model performance
 - We also need to tune hyperparameters
 #### Comments
 - Any of the above are good things for you guys to do
 - when in doubt copy the notebook when you edit to avoid merge conflicts

# TODO
- [ ] tweet preprocessing - Amal
- [ ] tweet featurization - Amal
- [ ] tweet clasification - Amal
- [ ] comparing word featurization - Jonny
- [ ] comparing word composition - Fred
- [ ] comparing tweet featurization - Fred

# IDEAS
- [ ] extending a featurization mtd w/ twitter metadata
- [ ] including external link metadata
- [ ] 

MVP Problem: mood detection 

-Need to featurize tweets
-First solve the problem of classifying tweets as positive or negative

Tasks
-Analyze images 
-Pagerank for external links to determine reputable sources and then parse the page
-Make amount of shares/likes per tweet a feature
-Bag of words
-word2vec
-LSI
-LDA
-doc2vec

-Best way for featurizing words
-Best way for aggregating word vectors into document vectors
-Best hyperparameter sweep for training the model


Amal
-MVP with mood detection 

Jerry

Jonny

Fred

