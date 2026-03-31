class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # s is the number of rows the string is stretched across in a zig zag pattern
        # so if we look at the pattern as a matrix
        # s the number of rows

        # if numRows is 1, return string. No processing needed.
        if numRows == 1:
            return s

        # create matrix, list of lists, equal to num of rows
        matrix = [[] for _ in range(numRows)]
        
        # counter to keep track of what row(list) we are appending to
        currentRow = 0 

        # direction indicator -1 for down, 1 for up. We start going down.
        direction = -1

        for c in s:
            # add the char to the correct list
            matrix[currentRow].append(c)
            # if we are at the top or bottom, flip direction
            if currentRow == 0 or currentRow == (numRows - 1):
                direction = -direction
            # move to the correct list, up or down
            currentRow += direction
            
        return ''.join(chain(*matrix))