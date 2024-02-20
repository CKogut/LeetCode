class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        flowers = n
        
        if flowers == 0:
            return True
            
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i==0 or flowerbed[i-1] == 0) and (i==len(flowerbed)-1 or flowerbed[i+1] ==0):
                flowerbed[i] = 1
                flowers -= 1
                if flowers == 0:
                    return True
        
        return False
             
            
   