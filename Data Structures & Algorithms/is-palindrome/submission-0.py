class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = s.lower()
        s = ''.join(char for char in s if char.isalnum())
        SIZE = len(s)
        L, R = 0, SIZE - 1

        for _ in range(len(s)):
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        
        return True