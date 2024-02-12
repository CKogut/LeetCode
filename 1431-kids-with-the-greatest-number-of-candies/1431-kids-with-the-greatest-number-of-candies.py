class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        lst = []
        
        for x in candies:
            if x + extraCandies >= max(candies):
                lst.append(True)
            else:
                lst.append(False)
                
        return lst