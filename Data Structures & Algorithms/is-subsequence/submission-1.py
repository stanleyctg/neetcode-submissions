class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr_s = 0
        if len(s) == 0:
            return True
        
        for i in range(len(t)):
            if t[i] == s[ptr_s]:
                ptr_s += 1
            if ptr_s == len(s):
                return True
        
        return False