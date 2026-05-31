class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            n = self.sum_square(n)
            if n in seen:
                return False
            seen.add(n)
        return True
    
    def sum_square(self, n: int) -> int:
        str_n = str(n)
        total = 0
        for digit in str_n:
            total += int(digit) ** 2
        return total

        