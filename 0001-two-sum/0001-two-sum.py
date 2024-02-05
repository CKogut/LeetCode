class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for index, value in enumerate(nums):
            value2 = target - value 
            for x in range(index+1, len(nums)):
                if nums[x] == value2:
                    return index, x
                else:
                    x+=1


