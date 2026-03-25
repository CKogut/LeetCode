class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # checking all possible strings to see if they're valid, and tracking length would be the naive
        # approach 

        # each char is potentially the center of the longest palindrome.
        # if we look at each char and then expand the left and right, we can quit looking 
        # when l or r goes out of bounds or invalidates the palindrome
        # so that should save some time I think.
        # Remember palindromes can be even or odd length, so "center" could be one or two chars
        
        # So... how to do that?

        # Track the indices of the longest valid string
        resStart, resLen = 0, 0

        for i in range(len(s)):
            # odd, sets center as 1 char
            l, r = i, i
            # while in bounds and the window is a valid palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # if this valid substring is longer then the currently stored valid substring
                if(r - l + 1) > resLen:
                    resStart = l
                    resLen = r - l + 1
                # exapand the window
                l -= 1
                r += 1
            
            # now check for even length palindromes
            l, r = i, i + 1
             # while in bounds and the window is a valid palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # if this valid substring is longer then the currently stored valid substring
                if(r - l + 1) > resLen:
                    resStart = l
                    resLen = r - l + 1
                # exapand the window
                l -= 1
                r += 1   

        # Return slice of the correct length from the starting index
        return s[resStart: resStart + resLen]