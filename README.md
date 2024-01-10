# brazilian-lotteries

## About the project

To analyze the **two lottery problems** and then publish an article in a scientific journal.

**Problem 1:** Is it possible to have a minimum number of bets (betting pool) that ensures the bettor receives at least one of the secondary prizes?

**Problem 2:** Is it possible to identify any bias in the lottery? If so, is it possible to generate a strategy that significantly increases the bettor's outcome?

"Problem 1" is closely linked to the famous "Traveling Salesman Problem" and, also having a polynomial analytical solution, can shed light on the P vs NP problem.


## Motivation

Since 2019, I have been studying Brazilian lotteries as a hobby, not with a predictive approach, but rather a deterministic one. The goal has always been to develop an algorithm that could generate a minimum number of bets in a game to guarantee that at least one bet would win at least a secondary prize.

In this project, that issue has been resolved. Therefore, I was motivated to explore whether Brazilian lotteries could also have any bias or tendency, and if they do, how to exploit them.

## A brief explanation of Brazilian lotteries

In Brazil, all lotteries are managed by the federal government, and there are a total of 11 official lotteries:
- only one lottery is sold as a ticket where the player does not have the right to choose the number;
- the other 10 lotteries are based on numbers that the player can choose;
- the most famous lottery is Mega-Sena, which has been around since 1996, and the prize is always above one million Brazilian currency units. However, the most popular lottery is Quina, with about 5.8 million bettors for each draw, and it has been around since 1994;
- to bet on Quina, just choose 5 numbers out of a total of 80 and then hope to be the winner.

## Chosen Lottery

Among the lotteries mentioned above, **Lotofacil** was chosen for the following reasons:
- it has many draws (more than 2 thousand);
- each number has a 60% probability of being drawn, and a pair of numbers also has a 35% probability of being drawn;
- a bet is formed with a large quantity of numbers, where 15 numbers must be chosen from a total of 25 numbers.

   
## Important Concepts
**bet:** an individual bet placed by a player

**betting pool:** a set of bets

**p-tuple:** a subset of p numbers from a bet

**Complete *p-betting pool:*** a game that contains the minimum number of bets that ensure at least one bet will win at least a secondary prize that requires ***p*** numbers or more to be matched in at least one bet.

**Spread factor:** it is the probability that at least one bet in the game will win at least a secondary prize in a draw.

**Complementary bet:** a bet in which the 10 numbers are different from another bet (this applies only in the brazilian Lotofácil lottery).


## Statistical and mathematical models used

Binomial distribution

Log-normal distribution

Hypothesis testing

**Supervised Learning**
- Naive Bayes
- Decision Trees
- Probability calibration
- Neural Network Models

**Unsupervised learning**
- Clustering
- Covariance estimation
- Neural networks models (usupervised)


## Python libraries used
- Pandas
- Scikit-learn
- Matplotlib

## Technologies used
- Python
- csv / xlsx
- JavaScript / HTML / CSS

## Author

Elisama O. Santos
- Data Scientist | Electronic Engineer
- elisamadeoliveira@hotmail.com
