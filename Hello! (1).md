

#**Soccer Match Outcome Prediction**


####By Bingzhe Cheng, Zheng Feng, Weijia Mao

----------


####**Objective**


Our object is to predict the outcome of European soccer matches from 2008 to 2016 given the detailed match information which includes both teams’ player info, betting odds from different providers, etc. 



#### <i class="icon-file"></i> **Data set**


We used three data sets. The first one contains more than 25,000 European soccer matches and their information from 2008 to 2016, such as scores, lineup players’ id, team formation and events. The second file consists of the betting odds for each match. The last one has all players and teams attributes from EA Sports FIFA games. We believe that FIFA gives relatively accurate ratings for players since it puts a lot of efforts into estimating players’ abilities. It uses a network of over 9,000 members to do a throughout review on each player. 

> - Scores, lineup, team formation and events
http://football-data.mx-api.enetscores.com/ 
> - Betting odds
http://www.football-data.co.uk/ 
> - Players and teams attributes from EA Sports FIFA games
http://sofifa.com/ 

#### **Visualization**
![Overall Rating](https://lh3.googleusercontent.com/-V5pO6GcvtpA/WfO0gK4eUCI/AAAAAAAABcM/j4UDKngkqigohGNnc7YpJMuY8LtXNtTegCLcBGAs/s0/Overall_rating.png "Overall_rating")
This graph shows the distribution of the overall ratings of every player.

![enter image description here](https://lh3.googleusercontent.com/-QrZFeOSsga8/WfO01o4ARCI/AAAAAAAABcU/1opEL5vlb0g2v0xVWZ_tdRUy2DvJal-JACLcBGAs/s0/match_outcome.png "match_outcome")
This pie chart shows the distribution of the outcome of every soccer match.

#### <i class="icon-trash"></i> **Cleaning corrupted or missing data**
We deleted the matches that miss one or more players’ id info. There are 4,605 of them out of 25,979. 

#### <i class="icon-hdd"></i> **Data processing**
1. We added a column called “result” that takes three values: 1,0, or -1. This is going to be our output space. “1” represents home team winning the match, “-1” represents away team winning the match, and “0” means the match resulted in a draw. This column is calculated by comparing the number of goals scored by the home team and the number of goals scored by the away team.

2. For our input space “X”, each row represents one match. The first 22 columns are the overall ratings for each startup player in the home team and the away team. We used the players’ id provided in the match information file and linked to the players’ rating provided by the player’s ability file. 
The 23rd column is calculated from the betting odds. It takes value “1” when most people predicted that the home team would win, “0” when most people predicted that the match would result in a draw, and “-1” when most people predicted that the away team would win.
The 24th column consists of ones to serve as the offset.

To summarize, our input space is a 21374 by 24 matrix. The output space is a column vector with length 21374.

#### <i class="icon-folder-open"></i> **The models we tried**
1. We tried several models. The first one was a linear regression model, where we add a column of ones as offsets to our input space. We understand that this is a classification problem and it is not the best idea to use linear regression. However the output space is {1,0,-1} and the bigger the output is, the better it is for the home team. We expect the home team players’ rating to be positively correlated with the result and the away team player’s rating to be negatively correlated with the result. Using linear regression and looking at the coefficient can give us a sense that whether our reasoning is correct. 

 After running linear regression, our resulting coefficients is as follows:
![enter image description here](https://lh3.googleusercontent.com/-hQX7Iy5-jzY/WfO37K7Z6iI/AAAAAAAABco/ogDEEym8HNkpvt9_E9noRLDQ32RzqkiUwCLcBGAs/s0/%25E5%25B1%258F%25E5%25B9%2595%25E5%25BF%25AB%25E7%2585%25A7+2017-10-27+%25E4%25B8%258B%25E5%258D%25886.48.27.png "w")

 (w_Hi is the coefficient of the ith home player, w_Hi is the coefficient of the ith away player, w_b is the coefficient of the 23rd column and w_o is the coefficient of the offset )
As we can see, except for the coefficients of one home player, all other coefficients are as expected. 

2. Next, we ran a random forest algorithm on our data. We took max feature m=sqrt(p), where p=23 is the number of columns of X. We took 80% of data in X as the training set and did the prediction on the remaining test data. As a result we managed to correctly predict 53% of the outcome in the our test set, which is 52% better than the randomly guess probability of 33%. 

#### <i class="icon-pencil"></i> **How to avoid overfitting?**
Since we implemented random forest algorithm, it has already used averaging to improve the predictive accuracy and controlled over-fitting.

####**How to test the effectiveness of the model?**
We would like to run test set on this model. We have trained the model with a precision of around 80% in the sample.

####**What remains to be done?**
For further exploration, we would like to add more features to our input space. For example, we could use the home team and away team’s recent match record because the match record implies whether the team is in a good form recently. Another set of data we want to further investigate is each player’s lineup position and their individual ability values. For example, a player who is put at the forward position would better contribute the team if he has good shooting skill. By adding features that reflect the player’s contribution to the team at the specific position, we might be able to better estimate the outcome of matches. 


