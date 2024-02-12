class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = 0
        longest_word = None
        
        if len(word1) < len(word2):
            n = len(word1)
            longest_word = word2
        else:
            n = len(word2)
            longest_word = word1
            
        merged = ""
        for i in range(0,n):
            merged += (word1[i])
            merged += (word2[i])
        
        if n < len(longest_word):
            merged += longest_word[n:]
    
        return merged