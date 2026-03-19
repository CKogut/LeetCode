class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # This is the brute force method
        # The arrays do NOT need to be combined and resorted, as they are already sorted
        # I will resubmit with a more efficient version once I can understand and fully explain

        combined = nums1 + nums2
        combined.sort()
        length = len(combined)

        if length % 2 == 1:
            return float(combined[length/2])
        else:
            return (float(combined[length/2-1]) + float(combined[length/2])) / 2
             