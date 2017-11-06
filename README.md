## 11-5-17  Report
### Amal
- beautified notebook and streamlined/standardized ML pipeline
- added more classifiers
- added some comments to explain some esoteric stuff I forgot why I did
- also guys for future reference please BRANCH instead of FORK from the repo - its much easier to manage IMO
- converted apiTest nb to python tweet crawler and made run script and sample tweet json
#### TODO
 - [ ] used word2vec for this pass -- but will also try w/ LDA/LSI/docv2vec as well
 - [ ] @Fred the above featurization schemes should answer your question as to the different ways to featurize the tweets - I will tentatively assign comparison to you
 - [ ] Note also there is no preprocessing - which should improve model performance
 - [ ] We also need to tune hyperparameters
#### Comments
 - Any of the above are good things for you guys to do
 - when in doubt copy the notebook when you edit to avoid merge conflicts
 - guys for future reference please BRANCH instead of FORK from the repo - its much easier to manage IMO

## Midterm report TODO
### Amal
- [x] @Fred - it is very easy to use a mlp for classification - in general it will achieve similar performance as random forest but will take longer to train, making iterating other aspects of our model pipeline more difficult
- [x] I will add a mlp test in the notebook and include the time to demonstrate my point
only if we get a larger dataset will a richer model like a NN be usefull
- [x] also I am seeing a submission link for a crawler code - I'll de notebookify what I already did and make a sample tweet json
- [x] I'll add two new classifiers (SVC, MLP)
- [x] denotebookify crawler and create run script as well as sample tweet json file

### Jonny
- [ ] also @Jonny Hurwitz it is important you include the ROC and PR/RC plots and associated AUC statistics
- [ ] also pls add f1 score - it is a good way to combine recall and precision
- [ ] I'll add two new classifiers (SVC, MLP) and we can include the plots for those guys too
maybe have a quick discussion of relative merits
- [ ] I would also say a discussion of other features not currently being used is warranted (tweet date, user metadata, images, etc...)
- [ ] when you get a chance pls resolve merge conflicts and submit a pull request



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

