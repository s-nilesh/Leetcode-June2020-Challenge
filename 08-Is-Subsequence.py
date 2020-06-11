#PROBLEM
# Given a string s and a string t, check if s is subsequence of t.

# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

# Credits:
# Special thanks to @pbrother for adding this problem and creating all test cases.


# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false





#SOLUTION-1
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while j<len(s) and i<len(t):
            if t[i] == s[j]:
                j += 1
            i += 1
        return j==len(s)
        

#SOLUTION-1
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        result =""
        for i in s:
            if i in t:
                result+=i
                
                t=t[t.index(i)+1:]
               
             
        if result== s:
            return True


#SOLUTION-1
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        iter_target = iter(t)
        return all(char in iter_target for char in s)