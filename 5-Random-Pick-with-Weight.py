#PROBLEM
# Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

# Note:
# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10000 times.

# Example 1:
# Input: 
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]

# Example 2:
# Input: 
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]

# Explanation of Input Syntax:
# The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()



#SOLUTION-1
import random
import bisect
class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = list(w)
        for i in range(1, len(w)):
            self.prefix_sum[i] += self.prefix_sum[i-1]

    def pickIndex(self) -> int:
        target = random.randint(0, self.prefix_sum[-1]-1)
        return bisect.bisect_right(self.prefix_sum, target)
    
    

#SOLUTION-1
from bisect import bisect_left
from random import random

class Solution:

    def __init__(self, w: List[int]):
        wSum = sum(w)
        currSum = 0
        self.list = []
        for i in w:
            currSum += i / wSum
            self.list.append(currSum)
            
    def pickIndex(self) -> int:
        return bisect_left(self.list, random())