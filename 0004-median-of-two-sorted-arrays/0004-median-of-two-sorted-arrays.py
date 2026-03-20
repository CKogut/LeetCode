class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        if len(nums1) > len(nums2):     # swap the arrays so nums1 is smallest
            nums1, nums2 = nums2, nums1     

        x = len(nums1)          # get length of arrays
        y = len(nums2)

        lo, hi = 0, x   # create pointers, the maximum window we can look at of nums1
        
        while lo <= hi: # While that window is valid, do the below.
            # Set partitions for both arrays
            # Starts with nums1 midpoint
            partitionX = (lo + hi) // 2    
            # How many elements of nums2 are needed to create equalish partitions
            # If the total of x+y is odd, the left partition has the extra value
            partitionY = ((x + y + 1) // 2) - partitionX 

            # Now that we now where the partion goes, we need to grab the values on either side of both
            # arrays to compare.

            # And if the partion would create an out of bounds exception, this sets the value in 
            # question to -inf or inf, otherwise it's the value directly left or right of the partition
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            # Condition in which the partion is correct. All values on left are less than right
            # This is the evaluation across the arrays at the partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # Yay, we can find the median!
                if (x + y) % 2 == 0:        # For a total combined even array
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:                       # For a total combined odd array
                    return max(maxLeftX, maxLeftY)
            # Partition is NOT correct. Decide whether to shift the partition left or right in nums1
            elif maxLeftX > minRightY:
                hi = partitionX - 1
            else:
                lo = partitionX + 1