#first unique character in a string
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            if s.count(i)==1:
                return s.index(i)
        return -1
    
    
................................................................................................................................................................


#Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result=0
        i=0
        d={}
        for j in range(len(s)):
            if s[j] in d:
               i=max(i,d[s[j]]+1)
            result=max(result,(j-i+1))
            d[s[j]]=j
        return result

