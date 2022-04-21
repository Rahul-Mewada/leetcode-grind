'''
 0 1 2 3 4 5 6 7 8 91011121314151617              1 2 3 4 5 6
 1 0 0 0 0 0 0 0 0 0 0
 l                   r
 
 17 - 12 = 5
 num_planted = 5
       
 if nums[l] == nums[r] == 1:
    num_possible += (r - l - 1) // 3
    
 if nums[l] == 0 and nums[r] == 1 or (nums[l] == 1 and nums[r] == 0):
    num_possible += (r - l) // 2

 if nums[l] == 0 and nums[r] == 0:
    num_possible += (r - l + 1) // 2
 
    
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            num_planted = 0 if flowerbed[0] == 1 else 1
            return n <= num_planted
        if n == 0:
            return True
        
        left = 0
        right = 0
        num_planted = 0
        nums = flowerbed
        while right < len(flowerbed):
            print(left, right)
            if right != left and (right == len(flowerbed) - 1 or flowerbed[right] == 1):
                if nums[left] == 1 and nums[right] == 1:
                    num_planted += ((right - left - 2) // 2)
                elif (nums[left] == 0 and nums[right] == 1) or (nums[left] == 1 and nums[right] == 0):
                    num_planted += (right - left) // 2
                elif nums[left] == 0 and nums[right] == 0:
                    num_planted += ((right - left) // 2) + 1
                left = right
            right += 1
        print(num_planted)
        return n <= num_planted