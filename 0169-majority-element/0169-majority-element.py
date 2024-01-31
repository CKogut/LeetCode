class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = {}
        majority_count = 1
        majority_key = nums[0]
        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i]+=1
                if  dict1.get(i, 0) > majority_count:
                    majority_count = dict1[i]
                    majority_key = i
        return majority_key