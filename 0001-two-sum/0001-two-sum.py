class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, num in enumerate(nums):
            value2 = target - num
            if value2 in hashmap:
                return [i, hashmap[value2]]
            hashmap[num] = i
        return []