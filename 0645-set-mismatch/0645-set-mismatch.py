class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0,0]                #[repeated number, missing number]

        for i in range(len(nums)):
            count = nums.count(i+1)
            if count == 2:
                result[0] = i+1
            if count == 0:
                result[1] = i+1
            
        return result