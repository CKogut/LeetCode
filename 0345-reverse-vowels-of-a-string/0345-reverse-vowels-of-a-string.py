class Solution:
    def reverseVowels(self, s: str) -> str:
        
        VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels = []
        slist = list(s)
        
        for i in range(len(slist)):
            if slist[i] in VOWELS:
                vowels.append(slist[i])
        
        
        current = len(vowels)-1
        
        for i in range(len(slist)):
            if slist[i] in VOWELS:
                slist[i] = vowels[current]
                current -= 1
        
        
        
        return ''.join(slist)