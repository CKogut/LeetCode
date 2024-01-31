class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 2
        while x < len(nums):
            if nums[x] == nums[x-1] and nums[x] == nums[x-2]:
                nums.pop(x)
            else:
                x+=1
        return len(nums)