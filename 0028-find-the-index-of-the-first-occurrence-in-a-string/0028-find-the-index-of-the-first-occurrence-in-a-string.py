class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        
        if needle in haystack:
            return haystack.index(needle)
        
        return index