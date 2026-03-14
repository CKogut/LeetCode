class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = list(nums)
        count = 0
        while count < len(nums):
            x = nums[count]
            result.append(x)
            count+=1

        return result