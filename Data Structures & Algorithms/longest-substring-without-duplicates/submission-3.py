class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        l = 0
        window_set = set()

        for r in range(len(s)):
            while s[r] in window_set:
                window_set.remove(s[l])
                l += 1
            window_set.add(s[r])
        
            max_length = max(len(window_set), max_length)
        return max_length
            
            
