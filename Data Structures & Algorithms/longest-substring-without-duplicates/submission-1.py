class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        l = 0

        for r in range(len(s)):
            # before inserting to sub_str check if its inside?
            while s[r] in s[l:r]:
                l += 1
            max_length = max(len(s[l:r+1]), max_length)
        
        return max_length
            
