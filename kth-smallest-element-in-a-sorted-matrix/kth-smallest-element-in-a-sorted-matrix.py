'''
[           !
    1,  5,  9
   10, 11, 13
   12, 13, 15
]
target = 4th largest 

Bin Seach of a Matrix

'''

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        mmin = matrix[0][0]     # top left 
        mmax = matrix[-1][-1]  # bottom right
        target = k
        
        while mmin < mmax:
            mid = (mmin + mmax)//2
            nums = self.count(matrix, mid)
            if nums < target:
                mmin = mid + 1
            else:
                mmax = mid
                
        return mmax
            
    def count(self, matrix, target):
        row = 0
        col = len(matrix) - 1
        count = 0
        while(row <= len(matrix)-1 and col >= 0):
            if matrix[row][col] <= target:
                count += col + 1
                row += 1
            else:
                col -= 1
        return count
            