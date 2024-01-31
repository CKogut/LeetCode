class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        max_count = 1
        temp_count = 1
        majority_element = nums[0]
        x = 1
        for x in range(len(nums)):
            if nums[x] == nums[x-1]:
                temp_count+=1
                if temp_count > max_count:
                    max_count = temp_count
                    majority_element = nums[x]
            else:
                temp_count = 1
                
            
        return majority_element