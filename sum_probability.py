import functools # import functools to act on or return other functions
import numpy as np 

@functools.lru_cache(maxsize=None) # decorator to wrap our probability function for caching
def probability(m: int, n: int) -> float:
    
   num_faces = 6 
   max_m = n * num_faces # maximum sum one can get for rolling n dice 
   min_m = n
   
   total_possible_outcomes = num_faces ** n # for each dice roll possible outcomes is equal to num of faces 
   
   # get trivial probabilties first given integer inputs m and n
   if m < min_m or m > max_m:
       
       return 0.00
   
   # Initialize ways_to_sum matrix where rows is the number of dices rolled and columns are the possible non-negative sums 
   ways_to_sum = np.zeros((n + 1, m + 1), dtype=int)
   ways_to_sum[0][0] = 1  # One unique way to get 0 sum which is rolling 0 dices, this will be used as a base counting number 
       
   # populate the ways_to_sum matrix generating clicks 
   for i in range(1, n + 1): # iterate through possible numbers of dice 
           
       for j in range(1, m + 1): 
                      
           for k in range(1, num_faces + 1): # iterate through all possible sums 
                  
               if j - k >= 0: # for a given sum j in the loop check if it is possible to have this roll
                      
                   ways_to_sum[i][j] += ways_to_sum[i - 1][j - k] # if one gets all the checks update
                   # Sum the number of ways to get (j-1), (j-2), ..., (j-6) with (i-1) dice
    
   # The result is the number of ways to get sum m with n dice
   num_of_waysmn = ways_to_sum[n][m]
    
   return num_of_waysmn/total_possible_outcomes
       
       
        
