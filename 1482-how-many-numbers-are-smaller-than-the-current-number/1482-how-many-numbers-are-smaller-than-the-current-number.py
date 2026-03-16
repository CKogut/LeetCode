class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)      # create sorted list
                                        # the index of the first occurence of a number tells you how many
                                        # other numbers are smaller 
        counts = {}                     # create dictionary to store counts of smaller numbets

        for index, num in enumerate(sorted_nums):
            if num not in counts:     # ignore repeated numbers
                counts[num] = index     # captures number as key and the index the value
        result = [counts[num] for num in nums]
        return result