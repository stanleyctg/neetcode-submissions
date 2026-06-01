class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        l = 0

        for r in range(len(s)):
            while len(set(s[l:r+1])) < len(s[l:r+1]):
                l += 1
            max_length = max(len(s[l:r+1]), max_length)
        
        return max_length
            
