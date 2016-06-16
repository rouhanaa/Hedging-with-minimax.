# Hedging-with-minimax. #
##Alexandra Rouhana's Final Year Project##


###What is it ?###
The main objective of this project was to implement a minimax algorithm mimicking the Black-Scholes hedging strategy.
 A game between the Investor and the Market was simulated. 
 This game has been divided into multiple trading periods during which  both players select in turn their future actions from a predefined set. For the Investor, finding the best move essentially comes to minimize his losses knowing that the adversary, the Market will want to maximize them. 
 
 
###What are the different files included in the repository?###
* The file "minimax" contains the main code running the algorithm.
* The file "parameters" needs to be included in the same folder as the minimax code.
* The file "bs_closed_form" contains an implementation of the BS equations for EC options.
* The file "bs_closed_implied vol" contains an implementation of the Newton Algorithm to compute the implied volatility. 

 ### How to run the code?###
 To run this code you will need: 
  * Python 2.7
  * The Python libraries numpy and scipy
             
