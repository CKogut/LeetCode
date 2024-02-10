class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0 or (x != 0 and x // 10 != 0):
            y = str(x)
            return y[::-1] == y
        
