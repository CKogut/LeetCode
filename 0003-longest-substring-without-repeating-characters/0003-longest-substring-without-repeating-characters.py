class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        char_set = set()                    # create empty set
        left = 0                            # set left pointer for sliding window
        max_length = 0                      # initialize maximum length counter

        for right in range(len(s)):         
            while s[right] in char_set:     # this will trigger when the window is INVALID (i.e. a repeated character)
                char_set.remove(s[left])    # remove the char from the set
                left += 1                   # move the left side of the windwow

            char_set.add(s[right])          # this is where to for loop will actually start, adds VALID char (i.e. unique char) to set
            current_window_size = right - left + 1              # shift the right side of the window 
            max_length = max(max_length, current_window_size)   # change max length if the current valid window is longer

        return max_length