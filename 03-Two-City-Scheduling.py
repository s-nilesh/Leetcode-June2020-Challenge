#PROBLEM
# There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

# Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

# Example 1:

# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation: 
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.
# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

# Note:
# 1 <= costs.length <= 100
# It is guaranteed that costs.length is even.
# 1 <= costs[i][0], costs[i][1] <= 1000



# SOLUTION-1
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # A,B=[],[]
        costs = sorted(costs, key=lambda x: abs(x[0]-x[1]), reverse=True)     #sorted costs in descending order with respect to the difference in cost
        ans, ca, cb, N = 0,0,0, len(costs)//2
        for x in costs:
            if (x[0]<x[1] and ca<N) or cb==N:
                ans += x[0]
                ca += 1
                # A.append(x[0])    #sanity checks
            else:
                ans += x[1]
                cb += 1
                # B.append(x[1])    #sanity checks
        return ans
    
    
# SOLUTION-2 
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x : x[0] - x[1])
        count, ans = len(costs)//2, 0
        for cost in costs:
            if count > 0:
                ans += cost[0]
            else:
                ans += cost[1]
            count -= 1
        return ans