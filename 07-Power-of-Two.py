#PROBLEM
# Given an integer, write a function to determine if it is a power of two.

# Example 1:
# Input: 1
# Output: true 
# Explanation: 20 = 1

# Example 2:
# Input: 16
# Output: true
# Explanation: 2^4 = 16

# Example 3:
# Input: 218
# Output: false



#SOLUTIONS
from math import log
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # return False if (log(n,2) - int(log(n,2))) else True
        # return n > 0 and (n & (n - 1)) == 0
        return n > 0 and (n & ~-n) == 0