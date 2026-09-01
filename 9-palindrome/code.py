class Solution:
    def isPalindrome(self, x) -> bool:
        digits = []

        if x < 0: x = -x; is_neg = True
        else: is_neg = False

        while x > 0:
            y = x % 10; x //= 10
            digits.append(y)
        
        if is_neg: digits.append("-")

        if digits == digits[::-1]: return True
        else: return False

