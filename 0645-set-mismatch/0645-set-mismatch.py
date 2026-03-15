class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        countList = [0] * (len(nums))     #list of place holding 0s
        result = [0,0]                      #[repeated number, missing number]

        for i in range(len(nums)):      
            value = nums[i]
            countList[value-1] += 1
            
        result[0] = countList.index(2)+1
        result[1] = countList.index(0)+1
        return result