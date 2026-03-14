class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        # nums is a list. it is twice the size on n. 
        # we want to split nums at the half way point, creating list x and y
        # next we merge the two list back together in a zippered manner (x1, y1, x2, y2...)

        x = nums[0:n]               # slice the list into the first half
        y = nums[n:len(nums)]       # slice the list into the second half
        result = []

        for i in range(n):          # iterate the length of the new lists 
            result.append(x[i])     # add xn
            result.append(y[i])     # add yn
        return result