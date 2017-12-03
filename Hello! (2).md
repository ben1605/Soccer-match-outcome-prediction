
<p align="center">
	<img style="float:center;" src="https://lh3.googleusercontent.com/-HJhKTYOsxsY/WiRQHnOCrAI/AAAAAAAABfA/ofzxnOohMCck7TRzctrzwWRWG3svq4qdACLcBGAs/s0/Screen+Shot+2017-12-03+at+1.45.35+AM.png")>
</p>	
<p align="center">
	<font size="7" color="FF3300">
		<b>ORIE 4741
	</font>
</p>	
<p align="center">
	<font size="60" color="black">
		<i> Final Project
	</font>
</p>	
<p align="center">
	<font size="6" color="black">
    <b>Soccer Match Outcome Prediction
</p>
<p align="center">
  <img src="http://s.4cdn.org/image/title/105.gif">
</p>
<p align="center">
	<font size="5" color="black">
Zheng Feng, zf72<br>                                     
Bingzhe Cheng, bc638<br>
 Weijia Mao, wm329  
 </font>
 </p>   


----------
<font size="6" color="black">
<b>Contents
</font>

<ol>
  <li>Project Introduction</li>
    <ul>
	1.1 Introduction<br>
	1.2 Objective   
    </ul> 
  <li>Data Processing and Visualization
    <ul>
    2.1 Data Description<br>
    2.2 Data Cleaning<br>
    2.3 Data Processing
	<ul>
		2.3.1 Team Formation<br>
		2.3.2. Player's Rating<br>
		2.3.3. Variance of Player's Rating<br>
		2.3.4. Head to Head record<br>
		2.3.5. The Betting Odds<br>
		2.3.6. The Output Space<br>
	</ul>	
    </ul>
  </li>
  <li>Models
	  <ul>
		3.1 Linear Regression<br>
		3.2 Decision Tree (Random Forest)<br>
		3.3 Multiclass Classification (Binary Encoding)<br>
		  <ul>
			3.3.1 Perceptron Algorithm<br>
			3.3.2 Hinge Loss<br>
		  </ul>
	  </ul>	  
  </li>
  <li> Conclusion</li>
	  
</ol>

**1. Project Introduction**
---------------

### 1.1 Introduction
Soccer is the most popular sport in the world. Every year thousands of professional soccer matches were played among the best soccer players in the world. We were often given the impression that soccer matches, unlike other sports, are hard to predict. It is not uncommon that an underdog team upsets a team with many superstars.

We are all fanatic soccer fans, and are interested in finding ways to predict the outcomes of matches more precisely. We found datasets from the internet that contain detailed information about different teams and players and matches they played. We decided that with the help of big data, we can make more precise predictions on soccer match outcomes. 

### 1.2 Objective
Our objective is to develop models base on the data we have to predict soccer match outcomes.

-------------------
**2. Data Processing and Visualization**
-
### 2.1 Data description
We used three data sets. The first one contains more than 25,000 European soccer matches and their information from 2008 to 2016, such as scores, lineup players’ id, team formation and events. The second file consists of the betting odds for each match. The last one has all players and teams attributes from EA Sports FIFA games. We believe that FIFA gives relatively accurate ratings for players since it puts a lot of efforts into estimating players’ abilities. It uses a network of over 9,000 members to do a throughout review on each player. 

1. Scores, lineup, team formation and events

http://football-data.mx-api.enetscores.com/ 

2. Betting odds

http://www.football-data.co.uk/ 

3. Players and teams attributes from EA Sports FIFA games

http://sofifa.com/ 

<p align="center">
	<img style="float:center;" src="https://lh3.googleusercontent.com/CdoxumWjuI4A_Yz8iFcBuFJWnmwHdw0eMa6dPSG1xOS9mXenXA6wUD-Ezl5axNoDkXzO62dWionH=s800")

<br>
<p>
	<i>This graph shows the distribution of the overall ratings of every player.
</p>

<p align="center">
	<img style="float:center;" src="https://lh3.googleusercontent.com/SGgqwBfw-3K6hWEyJn050NEi2TR1-U5vTse17EYcxUV6kNp1_fro9SsVKzODv_V84hgDl3tXpEiS=s1000")
</p>
<p>
	This pie chart shows the distribution of the outcome of every soccer match.
</p>

### 2.2 Data Cleaning
We deleted the matches that miss one or more players’ id info. There are 4,605 of them out of 25,979. 
### 2.3 Data Processing
Data processing is an important step in our project. 

#### 2.3.1 Team Formation
In our dataset, we found that there are 44 columns which indicate the position of players in each match. Specifically, each starting home player and away player has two columns indicating their X-coordinate and Y-coordinate in the field. We extracted the position of each players in each match from the dataset, and since there are a lot of duplicates, we removed all the repeating formations, and finally came up with 35 different formations. We plotted the following four formations as examples. 

![enter image description here](https://lh3.googleusercontent.com/Iy65Hu5nRZf88FkE_idmD6RQI0JWMMNyfJzYsC02ZOVLMeuae-3bGGgIK0Z448vV_rs1bwWBF9W7=s350 "formation1.png") ![enter image description here](https://lh3.googleusercontent.com/dbzUCHq208zhwtqtos4eqc5_balQOQGizDmePR0FJ14PpSH7oeJYoQ7OhuF63PkSGlV-8LTuVZuh=s350 "formation2.png")

<p >   <b>   &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4-4-2 &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4-5-1
</p>
	
 ![enter image description here](https://lh3.googleusercontent.com/hH61mMnVRmZ27VMZa1gpolfEPJ_hkWeLOJCBSJEzH13FoCGN2i_Hx3ehS6U1KT24F6ngb1fGvhsI=s350 "formation3.png")  ![enter image description here](https://lh3.googleusercontent.com/cW5tlcYSZxMC_I-RpH__E_AIHJ5nvJbonDlwC1GijE3Z6M_OM-0_es9gHUROoHXqLCXdQzS5GQf6=s350 "formation4.png")
 
 <p >   <b>   &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4-3-3 &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3-4-3
</p>
These graphs are some examples of commonly used formations. As shown in these graphs, there are generally four levels of players in each team, where the orange points represent forwards, red points represent midfields, blue points represent defenders, and green points represent goalkeepers. A formation of a team is determined by the number of forwards, midfielders, and defenders, and our goal is to transform the formation information into features for our project. Another thing needs to mention was that forwards and defenders are always in the same line (Y-coordinate), which made it more convenient to count their numbers, and by subtracting their sum from ten, we got the number of midfielders in each match. This is how we obtain the formation information from players’ position. 

We then added four columns of features to our data, they are: the number of forwards in the home team and away team, the number of defenders in the home team and away team. We left out the number of goalkeepers because it is always one. We left out the number of mid-fields to avoid collinearity.  

#### 2.3.2. Player’s rating
In our midterm report, our input space contains 22 columns of data representing the overall rating of each startup player in home team and away team. The correlation matrix is as follows: 

<p align="center">
	<img style="float:center;" src="https://lh3.googleusercontent.com/-I6DAFQvpYMk/WiRcxZXg5NI/AAAAAAAABgQ/Lvi9EZrfbn4CeudS4A3shR49Q_huutZbgCLcBGAs/s600/correlation+matrix.png")

</p><p>
As we can see, there is a strong positive correlation between the ratings of two players from the same team. This means that we can combine some of the players’ rating to reduce the total number of features. We grouped the players into four categories: goalkeeper, defender, midfielder and forward, and their correlation matrix is as follows: 
	</p>
<p align="center">
	<img style="float:center;" src="https://lh3.googleusercontent.com/-oRkJW6sg8Uo/WiRdU1IwAzI/AAAAAAAABgc/yRhGo2QjWKQb_oitetfo7-gvFgHPtSrBwCLcBGAs/s600/formation+matrix.png")
</p><p>
Again we can see that there are still strong correlations among these columns, so we decided to make all columns into two columns, one for home team and one for away team. We then calculated an overall score for each team base on the formula below:
</p>
Overall score = ($\Pi \ Player \ i's \ rating)^{1/k}$

The overall score is calculated by multiplying the ratings of all the players and take the kth root, where k is the number of players.

By this method, we get two features. They are home team and away team’s overall score. 

#### 2.3.3. Variance of player’s rating
Since soccer is a team sport, it is important that players on the same team should be at the same level to ensure good corporation. Therefore, we decided to calculate the variance of the home players’ ratings and away players’ ratings. We hypothesised that higher variance of the home team is negatively correlated with home team’s match result, while the higher variance of the away team is positively correlated with away team’s match result.

#### 2.3.4. Head to head record
In soccer, we often heard people saying that one team is particularly good or bad playing against another team. For example, The Chinese national soccer team is infamous for its bad record playing against the North Korea. In this case, the head to head record could capture this pattern that could not be captured by players’ individual ratings. 

Therefore, for each match, we look at all the matches played between the two teams before and calculate the home team’s winning rate, drawing rate, and losing rate. If there is no previous head to head record, we assign them to be ⅓ each.

We were able to get two new features. They are: home team’s winning rate and home team’s losing rate. We left out the home team’s drawing rate to avoid colinearity. 
####2.3.5. The betting odds
The betting odds reflect people’s anticipation of the result before a match takes place. We believe that it is a very useful feature because people who place their bets are usually the ones that do more research on the soccer teams and thus might have more insight knowledge about both team.
#### 2.3.6. The output space
The output space is the result of the matches. It is defined as follows:
$$Result =
\begin{cases}  
    1   & if \ home \  team \ wins \\
    \\
    0   & if \ two \ team \ draw\\
    \\
    -1 & if \ home\  team\ loses\\
\end{cases}$$

**3.  Models**
---
### 3.1 Linear Regression
Since our output space is {-1,0,1} and bigger number indicates that the home team does better, we were able to run a linear regression to test out the effect of each feature to the match result. After running linear regression, the coefficient vector is as follows:

![enter image description here](https://lh3.googleusercontent.com/-KzBrekgpQ1E/WiRli5jHRJI/AAAAAAAABhI/KVkPJtXa92I2dGAEeimmSPatoEMbPKuQgCLcBGAs/s800/Screen+Shot+2017-12-03+at+3.58.19+PM.png "Screen Shot 2017-12-03 at 3.58.19 PM.png")

where x1 is home team overall rating, x2 is away team overall rating, x3 is betting odds, x4 and x5 are home team’s number of defenders and forwards, x6 and x7 are away team’s number of defenders and forwards, x8 and x9 are home team and away team’s player rating variance, x10 and x11 are the winning rate and losing rate of the home team according to the historical head to head record. 

According to the p value, the first 3 coefficients are statistically significant. This is as expected. Besides home team’s number of defenders, the team’s formation does not seem to be very important. for the player’s rating variance x8 and x9, it is surprising that a higher variance actually contributes to the team’s match performance, it is opposite to what we hypothesized. It is also surprising that the historical head to head record is insignificant. One possible cause might be that the available data is not big enough for our regression to be meaningful.

#########test result####################

One thing to notice about linear regression is that although some of the features might seem to be insignificant, it does not mean that the features are useless. It might be because that the features and the matches results do not have a linear relationship. Later, we will apply a nonlinear model to see if we can make a better prediction.

### 3.2 Decision Tree (Random Forest)

### 3.3 Multiclass Classification (Binary Encoding)
#### 3.3.1 Perceptron Algorithm
#### 3.3.2 Hinge Loss

**4. Conclusion**
-







